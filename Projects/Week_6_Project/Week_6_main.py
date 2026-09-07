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
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/processed/weather.db")
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

    
if __name__ == "__main__":
    raw_data = extract()
    print(f"Extracted {len(raw_data)} records successfully!")