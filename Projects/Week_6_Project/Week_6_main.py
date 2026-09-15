import json
import logging
import os
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import requests
from sqlalchemy import create_engine, text

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

API_BASE_URL = os.getenv("API_BASE_URL", "https://earthquake.usgs.gov/fdsnws/event/1/query")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/processed/earthquakes.db")
RAW_PATH = Path("data/processed/etl_raw_earthquakes.json")
LOG_PATH = Path("data/processed/pipeline_runs.csv")


def extract(format: str = "geojson",starttime: str = None, endtime: str = None, minmagnitude: str = "2.5") -> list[dict]:

    if not starttime:
        starttime = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    if not endtime:
        endtime = datetime.now().strftime("%Y-%m-%d")

    logging.info("Extracting earthquake data from %s to %s", starttime, endtime)

    params = {
        "format": format,
        "starttime": starttime,
        "endtime": endtime,
        "minmagnitude": minmagnitude,
    }

    try:
        response = requests.get(API_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        features = data.get("features", [])
    except Exception as e:
        logging.error("Failed to fetch data: %s", e)
        features = [
            {
                "id": "fallback_0",
                "properties": {
                    "mag": 0.0,
                    "place": "Fallback Location",
                    "title": "M 0.0 - Fallback",
                    "time": 0,
                },
                "geometry": {"coordinates": [0.0, 0.0, 0.0]},
            }
        ]

    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
    RAW_PATH.write_text(json.dumps(features, indent=2), encoding="utf-8")

    return features


def transform(records: list[dict]) -> pd.DataFrame:
    logging.info("Transforming %d records", len(records))

    if not records:
        logging.warning("No records returned from API.")
        return pd.DataFrame(
            columns=[
                "id",
                "magnitude",
                "place",
                "title",
                "event_time",
                "longitude",
                "latitude",
                "depth",
                "loaded_at",
            ]
        )

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

<<<<<<< HEAD

=======
>>>>>>> e5a17e26a5c4fd411989f84e439851abc2102aad
    df["longitude"] = df["coordinates"].str[0].fillna(0.0)
    df["latitude"] = df["coordinates"].str[1].fillna(0.0)
    df["depth"] = df["coordinates"].str[2].fillna(0.0)
    df = df.drop(columns=["coordinates"])
    df["event_time"] = pd.to_datetime(df["event_time"], unit="ms")
    df["place"] = df["place"].fillna("Unknown Location")
    df["title"] = df["title"].fillna("Untitled Event")
    df["magnitude"] = df["magnitude"].fillna(0.0)
    df["loaded_at"] = datetime.now().isoformat(timespec="seconds")

    return df


def load(df: pd.DataFrame, table_name: str = "earthquakes") -> int:
    logging.info("Loading records into table '%s' at %s", table_name, DATABASE_URL)
    engine = create_engine(DATABASE_URL)
    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        count = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar_one()
    return count


def log_run(extracted_count: int, loaded_count: int) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log_df = pd.DataFrame(
        [
            {
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "extracted_count": extracted_count,
                "loaded_count": loaded_count,
            }
        ]
    )
    log_df.to_csv(LOG_PATH, mode="a", header=not LOG_PATH.exists(), index=False)
    logging.info("Execution log appended to %s", LOG_PATH)


if __name__ == "__main__":
    raw_data = extract()
    transformed_df = transform(raw_data)
    loaded_count = load(transformed_df)
    log_run(len(raw_data), loaded_count)

    print(f"\nPipeline run successful! Total earthquake records in DB: {loaded_count}")
