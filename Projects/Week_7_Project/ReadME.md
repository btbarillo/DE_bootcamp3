# Week 7 Project: Earthquake & User Countries ETL Pipeline using Google Cloud Platform

## Project Overview
To extract and process real-time earthquake data from the USGS API alongside user country risk profiles in order to identify high-risk seismic events and automatically trigger location-based alerts.


## Step-by-Step Implementation

### Step 1: Storage Setup (Google Cloud Storage)
- Set up a GCS Bucket (`gs://berns-earthquake-pipeline-gcp/`) with an organized folder structure for raw, processed, and script assets:
  - `/scripts/` – Stores the PySpark scripts (`job_earthquake_api.py` and `job_user_countries.py`)
  - `/raw/` – Landing storage for raw API ingestion data
  - `/processed/earthquakes/dt=YYYY-MM-DD/` – Output directory for processed earthquake CSV/Parquet files partitioned by date
  - `/processed/users/dt=YYYY-MM-DD/` – Output directory for the user/country reference dataset partitioned by date
  - `/reports/` – Storage for exported query results
<img width="1460" height="643" alt="image" src="https://github.com/user-attachments/assets/18b149b2-2ced-43f8-aa43-48ef1ad5de19" />



### Step 2: PySpark ETL Development (Dataproc Serverless)
**Step 2.1:** Generated two main PySpark batch scripts for data extraction and transformation:

- [job_earthquake_api.py](https://github.com/btbarillo/DE_bootcamp3/blob/master/Projects/Week_7_Project/job_earthquake_api.py) (Earthquake API Ingestion Job):
  - Connects to the USGS API to fetch earthquake data based on specified parameters (e.g., minmagnitude, starttime, endtime).
  - Converts and normalizes the GeoJSON/JSON response into a structured tabular format (e.g., id, place, magnitude, event_time, longitude, latitude).
  - Writes the transformed data back to GCS under `/processed/earthquakes/` using Hive-style partitioning (`dt=YYYY-MM-DD`).

- [job_user_countries.py](https://github.com/btbarillo/DE_bootcamp3/blob/master/Projects/Week_7_Project/job_user_countries.py) (User/Country Reference Job):
  - Processes the user countries and threshold profiles data.
  - Writes the clean data to GCS under `/processed/users/`.

**Step 2.2:** Set up the batches for both scripts on `Managed Apache Spark`and used **PySpark** as the batch type

<img width="1087" height="684" alt="image" src="https://github.com/user-attachments/assets/b2c3000c-b1d5-4c1c-82d8-09a474501b00" />

<img width="1392" height="309" alt="image" src="https://github.com/user-attachments/assets/21dd58f3-6c90-43f4-9f05-e84fe34edd78" />

### Step 3: Workflow Orchestration (Google Cloud Workflows)
Used Google Cloud Workflows to orchestrate our PySpark jobs on Google Cloud Dataproc Serverless.

### 1. Serverless Orchestration (`main workflow`)
* **Purpose:** Automatically triggers and controls the execution of PySpark batch jobs.
* **Key Feature:** Runs entirely serverless—no virtual machines or clusters need to be constantly managed or paid for when idle.

### 2. Sequential Job Execution
To ensure data dependency and integrity, the pipeline runs in a strict sequential order:
1. **`earthquake_job`:** Triggers `job_earthquake_api.py` to fetch, process, and save USGS earthquake data to Google Cloud Storage (GCS).
2. **`user_countries_job`:** Runs `job_user_countries.py` **only after** the earthquake job successfully completes.

### 3. Automatic Job Monitoring (*Polling*)
* **Status Checking:** The workflow automatically tracks the state of each Dataproc batch job.
* **Completion Handling:** It continuously monitors execution until the job returns a status of `SUCCEEDED` or `FAILED`.
* **Error Prevention:** If the first job fails, the pipeline automatically stops to prevent corrupted or incomplete downstream data processing.

---

## Workflow Execution Flow

```text
[Start Pipeline]
       │
       ▼
[1. Trigger Earthquake PySpark Job]
       │
       ▼
[Monitor Status until SUCCEEDED] ────► (If Failed: Stop Pipeline)
       │
       ▼
[2. Trigger User Countries Job]
       │
       ▼
[Monitor Status until SUCCEEDED] ────► (If Failed: Stop Pipeline)
       │
       ▼
[Pipeline Completed Successfully]
```

### Step 4: BigQuery Integration & External Tables
In BigQuery, I created the `berns_earthquake_db` dataset and configured external tables to query the data directly from GCS without duplicating or permanently importing files into the warehouse.

<img width="1242" height="428" alt="image" src="https://github.com/user-attachments/assets/b49caf6d-ba04-4c7a-872b-424a68e0c80e" />

`table_earthquakes`:

- Points to the GCS path: `gs://berns-earthquake-pipeline-gcp/processed/earthquakes/*.csv`
- Dynamically reads across all partitioned subfolders at once.

`table_user_countries`:

- Points to the GCS path: (`gs://berns-earthquake-pipeline-gcp/processed/users/*.csv`)
- Dynamically reads across all partitioned subfolders at once.

### Step 5: BigQuery SQL for Data Analysis

Because there is no direct Foreign Key or ID match between the USGS location string (e.g., `"12 km S of Malate, Philippines"`) and the reference dataset's `country_name` (e.g., `"Philippines"`), I used `REGEXP_CONTAINS` combined with Word Boundaries (`\b`) and `LOWER()` for case-insensitive exact substring matching.

Additionally, `SELECT DISTINCT` is applied to the reference dataset subquery to ensure clean 1-to-many joins.

**Conditional Alert Logic**

The query uses a conditional `CASE WHEN` evaluation to categorize events based on country-specific risk levels:

* **`CRITICAL ALERT`:** Triggered if an earthquake's magnitude is greater than or equal to the country's defined `risk_threshold_mag`.
* **`MONITOR`:** Assigned if the earthquake's magnitude falls below the designated threshold.

The analysis is saved in the reports folder under the bucket `berns-earthquake-pipeline-gcp`
<img width="1328" height="479" alt="image" src="https://github.com/user-attachments/assets/66d198bd-72bd-477c-85fd-1dd836532f9a" />

