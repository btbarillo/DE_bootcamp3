import json
import logging
import os
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import requests
from sqlalchemy import create_engine, text

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(messages)s")

API_BASE_URL = os.getenv("API_BASE_URL", "https://earthquake.usgs.gov/fdsnws/event/1/query")
DATABASE_URL= os.getenv("DATABASE_URL","sqlite:///data/processed/earthquakes.db")
RAW_PATH = Path("data/processed/etl_raw_earthquakes.json")
LOG_PATH = Path("data/processed/pipeline_runs.csv")


def extract(format: str="geojson", starttime: str = None, endtime: str = None, minmagnitude: str = "2.5") -> list[dict]:

    if not starttime:
        starttime = (datetime.now()- timedelta(days=7)).strftime("%Y-%m-%d")
    if not endtime:
        endtimte = datetime.now().strftime("%Y-%m-%d")

    logging.info("Extracting earthquake data from %s to %s", starttime, endtime)

    params={
        "format" = format,
        "starttime" = starttime,
        

    }