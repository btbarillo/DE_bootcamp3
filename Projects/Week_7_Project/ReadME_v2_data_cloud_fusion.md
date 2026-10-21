# Week 7 Project: Earthquake & User Countries ETL Pipeline using Google Cloud Platform

## Project Overview
To extract and process real-time earthquake data from the USGS API alongside user country risk profiles in order to identify high-risk seismic events and automatically trigger location-based alerts.


## Step-by-Step Implementation

## Step 1: Storage Setup (Google Cloud Storage)
- Set up a GCS Bucket (`gs://berns-earthquake-pipeline-gcp/`) with an organized folder structure for raw, processed, and script assets:
  - `/scripts/` – Stores the PySpark scripts (`job_earthquake_api.py` and `job_user_countries.py`)
  - `/raw/` – Landing storage for raw API ingestion data
  - `/processed/earthquakes/dt=YYYY-MM-DD/` – Output directory for processed earthquake CSV/Parquet files partitioned by date
  - `/processed/users/dt=YYYY-MM-DD/` – Output directory for the user/country reference dataset partitioned by date
  - `/reports/` – Storage for exported query results
<img width="1460" height="643" alt="image" src="https://github.com/user-attachments/assets/18b149b2-2ced-43f8-aa43-48ef1ad5de19" />


## Step 2: Cloud Data Fusion Ingestion Pipelines

### 1. Earthquake Data Pipeline (`pipeline-earthquake-ingestion`)

- **Source:** USGS REST API (`https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson`) via **HTTP Poller**.
- **Transform:** Extracted JSON payload using **Wrangler** directives (`parse-as-json :body`, `drop`).
- **Sink:** Saved processed data to `gs://berns-earthquake-pipeline-gcp/processed/earthquakes/`.


### 2. User Reference Data Pipeline (`pipeline-user-reference-ingestion`)

- **Source:** Static CSV file from `gs://berns-earthquake-pipeline-gcp/raw/` via **GCS Source**.
- **Transform:** Formatted schema (`Use First Row as Header: True`) and clean columns (`country_name`, `region`, `emergency_contact_email`, `risk_threshold_mag`) using **Wrangler**.
- **Sink:** Saved structured user records to `gs://berns-earthquake-pipeline-gcp/processed/users/`.

<img width="1439" height="727" alt="image" src="https://github.com/user-attachments/assets/88f3b444-f883-468e-bfde-cc8de3ab765d" />

<img width="1439" height="720" alt="image" src="https://github.com/user-attachments/assets/ab3dd002-9ef6-47d7-9857-3e9e714ccbd5" />


## Step 3: BigQuery Integration & External Tables
In BigQuery, I created the `berns_earthquake_db` dataset and configured external tables to query the data directly from GCS without duplicating or permanently importing files into the warehouse.

<img width="1242" height="428" alt="image" src="https://github.com/user-attachments/assets/b49caf6d-ba04-4c7a-872b-424a68e0c80e" />

`table_earthquakes`:

- Points to the GCS path: `gs://berns-earthquake-pipeline-gcp/processed/earthquakes/*.csv`
- Dynamically reads across all partitioned subfolders at once.

`table_user_countries`:

- Points to the GCS path: (`gs://berns-earthquake-pipeline-gcp/processed/users/*.csv`)
- Dynamically reads across all partitioned subfolders at once.

## Step 4: BigQuery SQL for Data Analysis

Because there is no direct Foreign Key or ID match between the USGS location string (e.g., `"12 km S of Malate, Philippines"`) and the reference dataset's `country_name` (e.g., `"Philippines"`), I used `REGEXP_CONTAINS` combined with Word Boundaries (`\b`) and `LOWER()` for case-insensitive exact substring matching.

Additionally, `SELECT DISTINCT` is applied to the reference dataset subquery to ensure clean 1-to-many joins.

**Conditional Alert Logic**

The query uses a conditional `CASE WHEN` evaluation to categorize events based on country-specific risk levels:

* **`CRITICAL ALERT`:** Triggered if an earthquake's magnitude is greater than or equal to the country's defined `risk_threshold_mag`.
* **`MONITOR`:** Assigned if the earthquake's magnitude falls below the designated threshold.

The analysis is saved in the reports folder under the bucket `berns-earthquake-pipeline-gcp`
<img width="1328" height="479" alt="image" src="https://github.com/user-attachments/assets/66d198bd-72bd-477c-85fd-1dd836532f9a" />

