import json
import logging
import os
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests
from sqlalchemy import create_engine, text


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.tvmaze.com/search/shows")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/processed/tv_shows.db")
RAW_PATH = Path("data/processed/etl_raw_tv_shows.json")
LOG_PATH = Path("data/processed/pipeline_runs.csv")

def extract(query: str="girls") -> list[dict]:
    url=f"{API_BASE_URL}?q={query}"
    logging.info("Extracting from %s", url)

    try:
        response = requests.get(url, timeout = 10)
        response.raise_for_status()
        data = response.json()
        if isinstance(data,dict):
            data = [data]
    except Exception as e:
        logging.error("Failed to fetch data: %s", e)
        data = [{"show": {"id": 0, "name": "Fallback Show", "type": "Scripted"}}]

    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
    RAW_PATH.write_text(json.dumps(data,indent=2), encoding="utf-8")

    return data

def transform(records: list[dict]) -> pd.DataFrame:
    logging.info("Transforming %d record", len(records))
    df = pd.json_normalize(records)
    column_mapping = {
        "show.id": "id",
        "show.name": "name",
        "show.type": "type",
        "show.language" :"language",
        "show.status":"status"
    }
    existing_cols = [col for col in column_mapping.keys() if col in df.columns]
    df = df[existing_cols].copy()
    df = df.rename(columns=column_mapping)
    df = df.fillna("Unknown")
    df["loaded_at"] = datetime.now().isoformat(timespec="seconds")

    return df


def load(df: pd.DataFrame, table_name: str = "tv_shows") -> int:
    logging.info("Loading to %s", DATABASE_URL)
    engine = create_engine(DATABASE_URL)
    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        count = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar_one()
    return count

def log_run(extracted_count: int, loaded_count: int) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log_df = pd.DataFrame([{
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "extracted_count": extracted_count,
        "loaded_count": loaded_count
    }])
    log_df.to_csv(LOG_PATH, mode="a", header=not LOG_PATH.exists(), index=False)
    logging.info("Execution log saved to %s", LOG_PATH)

    
if __name__ == "__main__":
    raw_data = extract()
    transformed_df = transform(raw_data)
    loaded_count = load(transformed_df)
    log_run(len(raw_data), loaded_count)
    
    print(f"\nPipeline run successful! Total records in DB: {loaded_count}")