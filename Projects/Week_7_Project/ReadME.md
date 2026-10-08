# Week 7 Project: Flight & User Countries ETL Pipeline using Google Cloud Platform

## Project Overview
In this project, 



## Step-by-Step Implementation

### Step 1: Storage Setup (Google Cloud Storage)
- Set up a GCS Bucket (`gs://berns-earthquake-pipeline-gcp/`) with an organized folder structure for raw, processed, and script assets:
  - `/scripts/` – Stores the PySpark scripts (`job_earthquake_api.py` and `job_user_countries.py`)
  - `/raw/` – Landing storage for raw API ingestion data
  - `/processed/earthquakes/dt=YYYY-MM-DD/` – Output directory for processed earthquake CSV/Parquet files partitioned by date
  - `/processed/user_countries/dt=YYYY-MM-DD/` – Output directory for the user/country reference dataset partitioned by date
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
  - Writes the clean data to GCS under `/processed/user_countries/`.

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
1. **`run_earthquake_job`:** Triggers `job_earthquake_api.py` to fetch, process, and save USGS earthquake data to Google Cloud Storage (GSC).
2. **`run_user_countries_job`:** Runs `job_user_countries.py` **only after** the earthquake job successfully completes.

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
To query the data without needing to duplicate or permanently import raw storage into the warehouse, external tables were set up:

`ext_earthquakes` Table:

- Points to the GCS path: gs://berns-earthquake-pipeline-gcp/processed/earthquakes/*.csv.

- Dynamically reads across all partitioned subfolders at once.

`ext_user_countries` Table:

- Points to the reference directory of the user countries data in GCS.

### Step 5: BigQuery SQL for Data Analysis
