# Week 7 Project: Flight & Users Data Pipeline

## Project Overview
This project demonstrates the end-to-end cloud migration of a local data pipeline to AWS. The main objective is to ingest both static ([flights_raw.csv](https://github.com/btbarillo/DE_bootcamp3/tree/master/data/raw/flights_raw.csv)) and dynamic (https://jsonplaceholder.typicode.com/users) datasets, store them securely in Amazon S3, structure their schemas, and perform SQL-based data integration and analytics using Amazon Athena.


## Project Objective
To combine flight operational data with user profiles to identify which specific passengers(including their info such as cities and email addresses) are impacted by flight delays.


## Step-by-Step Implementation

### Step 1: Environment & Credentials setup
- Created `.env` file for AWS Credentials to ensure sensitive keys are not exposed.

<img width="639" height="176" alt="image" src="https://github.com/user-attachments/assets/3920aa66-6874-45bf-8ab7-cb4c14e4d557" />

### Step 2: Data ingestion to Amazon S3
- Created and ran `upload_files_to_s3.py` to upload [flights_raw.csv](https://github.com/btbarillo/DE_bootcamp3/tree/master/data/raw/flights_raw.csv) to AWS S3
- Created and ran  `fetch_users_api.py` to fetch from the API https://jsonplaceholder.typicode.com/users and convert the API JSON to a local CSV, then uploaded the local CSV to AWS S3
<img width="1429" height="681" alt="image" src="https://github.com/user-attachments/assets/31801f8c-d480-4e64-b775-94d0bd24edfd" />
<img width="1148" height="436" alt="image" src="https://github.com/user-attachments/assets/5fb8a63c-cebb-4f9a-9782-d89c3664aee4" />
<img width="1134" height="454" alt="image" src="https://github.com/user-attachments/assets/01bb35a1-5829-4196-bf47-24f84bb0b3ee" />

