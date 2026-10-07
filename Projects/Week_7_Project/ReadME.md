# Week 7 Project: Flight & User Countries ETL Pipeline using Google Cloud Platform

## Project Overview
In this project, 



## Step-by-Step Implementation

### Step 1: Storage Setup (Google Cloud Storage)
- I set up a GCS Bucket (gs://berns-earthquake-pipeline-gcp/) with an organized folder structure for raw, processed, and script assets:
  - `/scripts/` – Stores the PySpark scripts (`job_earthquake_api.py` and `job_user_countries.py`)
  - `/raw/` – Landing storage for raw API ingestion data
  - `/processed/earthquakes/dt=YYYY-MM-DD/` – Output directory for processed earthquake CSV/Parquet files partitioned by date
  - `/processed/user_countries/dt=YYYY-MM-DD/` – Output directory for the user/country reference dataset partitioned by date
  - `/reports/` – Storage for exported query results
<img width="1460" height="643" alt="image" src="https://github.com/user-attachments/assets/18b149b2-2ced-43f8-aa43-48ef1ad5de19" />



### Step 2: PySpark ETL Development (Dataproc Serverless)


### Step 3: Workflow Orchestration (Google Cloud Workflows)


### Step 4: BigQuery Integration & External Tables


### Step 5: BigQuery SQL for Data Analysis
