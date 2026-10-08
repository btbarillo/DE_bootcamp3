import sys
import json
import logging
import requests
import pandas as pd
from datetime import datetime, timedelta, timezone
from io import StringIO
from google.cloud import storage

BUCKET_NAME = sys.argv[1] if len(sys.argv) > 1 else "berns-earthquake-pipeline-gcp"
storage_client = storage.Client()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def get_ph_now():
    return datetime.now(timezone.utc) + timedelta(hours=8)

def extract() -> list[dict]:

    start_utc = datetime.now(timezone.utc) - timedelta(days=7)
    starttime_str = start_utc.strftime("%Y-%m-%d")
    

    direct_url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={starttime_str}&minmagnitude=2.5"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    logging.info(f"Fetching USGS API via direct URL: {direct_url}")

    try:
        response = requests.get(direct_url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        features = data.get("features", [])
        
        logging.info(f"Successfully fetched {len(features)} live earthquake records.")

        if not features:
            raise ValueError("API returned empty list, retrying with past 30 days...")

    except Exception as err:
        logging.error(f"Primary fetch failed: {err}. Attempting fallback endpoint without magnitude filter...")
        backup_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson"
        response = requests.get(backup_url, headers=headers, timeout=30)
        data = response.json()
        features = data.get("features", [])

    today_ph_str = get_ph_now().strftime("%Y-%m-%d")
    raw_key = f"raw/earthquakes/{today_ph_str}/earthquakes_raw.json"

    try:
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(raw_key)
        blob.upload_from_string(json.dumps(features, indent=2), content_type="application/json")
        logging.info(f"Successfully saved raw JSON payload to gs://{BUCKET_NAME}/{raw_key}")
    except Exception as e:
        logging.warning(f"Could not upload raw JSON to GCS: {e}")

    return features


def transform(records: list[dict]) -> pd.DataFrame:
    logging.info(f"Transforming {len(records)} records")

    if not records:
        return pd.DataFrame(columns=["id", "magnitude", "place", "title", "event_time", "longitude", "latitude", "depth", "loaded_at"])

    df = pd.json_normalize(records)
    column_mapping = {
        "id": "id",
        "properties.mag": "magnitude",
        "properties.place": "place",
        "properties.title": "title",
        "properties.time": "event_time",
        "geometry.coordinates": "coordinates",
    }

    existing_cols = [col for col in column_mapping.keys() if col in df.columns]
    df = df[existing_cols].copy()
    df = df.rename(columns=column_mapping)

    df["longitude"] = df["coordinates"].str[0].fillna(0.0)
    df["latitude"] = df["coordinates"].str[1].fillna(0.0)
    df["depth"] = df["coordinates"].str[2].fillna(0.0)
    df = df.drop(columns=["coordinates"])

    df["event_time"] = pd.to_datetime(df["event_time"], unit="ms").dt.strftime('%Y-%m-%d %H:%M:%S')
    df["place"] = df["place"].fillna("Unknown Location")
    df["title"] = df["title"].fillna("Untitled Event")
    df["magnitude"] = df["magnitude"].fillna(0.0)
    
    df["loaded_at"] = get_ph_now().isoformat(timespec="seconds")

    return df


def load_to_gcs(df: pd.DataFrame) -> int:
    today_ph_str = get_ph_now().strftime("%Y-%m-%d")
    gcs_key = f"processed/earthquakes/dt={today_ph_str}/earthquakes_clean.csv"
    logging.info(f"Loading {len(df)} records into GCS bucket at gs://{BUCKET_NAME}/{gcs_key}")

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(gcs_key)
    blob.upload_from_string(csv_buffer.getvalue(), content_type="text/csv")
    logging.info(f"Successfully loaded clean data to GCS!")
    return len(df)


if __name__ == "__main__":
    raw_data = extract()
    transformed_df = transform(raw_data)

    if not transformed_df.empty:
        loaded_count = load_to_gcs(transformed_df)
        print(f"\nPipeline run successful! Total earthquake records loaded to GCS: {loaded_count}")
    else:
        print("\nNo records were transformed or loaded.")