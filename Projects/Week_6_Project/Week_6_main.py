import json
import logging
import os
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests
from sqlalchemy import create_engine, text


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

API_BASE_URL = os.getenv("API_URL", "https://api.tvmaze.com/search/shows")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/processed/weather.db")
RAW_PATH = Path("data/processed/etl_raw_tv_shows.json")
LOG_PATH = Path("data/processed/pipeline_runs.csv")

def extract(query: str="girls") -> list[dict]:
    url=f"{API_BASE_URL}?q={query}"
    logging.info("Extracting from %s", url)


    
