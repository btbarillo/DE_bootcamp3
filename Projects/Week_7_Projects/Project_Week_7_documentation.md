# Week 7 Project: Flight & Users Data Pipeline

## Project Overview
This project demonstrates the end-to-end cloud migration of a local data pipeline to AWS. The main objective is to ingest both static ([flights_raw.csv](https://github.com/btbarillo/DE_bootcamp3/tree/master/data/raw/flights_raw.csv)) and dynamic (https://jsonplaceholder.typicode.com/users) datasets, store them securely in Amazon S3, structure their schemas, and perform SQL-based data integration and analytics using Amazon Athena.


## Project Objective
To combine flight operational data with user profiles to identify which specific passengers(including their info such as cities and email addresses) are impacted by flight delays.


## Step-by-Step Implementation

### Step 1: Environment & Credentials setup
- Generated access keys on the AWS console for the `access key ID` and `secret access key`
- Created a `.env` file for AWS Credentials to ensure sensitive keys are not exposed.

<img width="639" height="176" alt="image" src="https://github.com/user-attachments/assets/3920aa66-6874-45bf-8ab7-cb4c14e4d557" />

### Step 2: Data ingestion to Amazon S3
- Created and ran `Week_7_upload_csv_to_s3.py` to upload [flights_raw.csv](https://github.com/btbarillo/DE_bootcamp3/tree/master/data/raw/flights_raw.csv) to AWS S3
- Created and ran  `Week_7_fetch_and_upload_api_users.py` to fetch from the API https://jsonplaceholder.typicode.com/users and convert the API JSON to a local CSV, then uploaded the local CSV to AWS S3
<img width="1429" height="681" alt="image" src="https://github.com/user-attachments/assets/31801f8c-d480-4e64-b775-94d0bd24edfd" />
<img width="1148" height="436" alt="image" src="https://github.com/user-attachments/assets/5fb8a63c-cebb-4f9a-9782-d89c3664aee4" />
<img width="1134" height="454" alt="image" src="https://github.com/user-attachments/assets/01bb35a1-5829-4196-bf47-24f84bb0b3ee" />


### Step 3: Schema Creation in Amazon Athena
- Created database manually in Athena DDL
<img width="1432" height="697" alt="image" src="https://github.com/user-attachments/assets/695a71f3-2673-41f1-9384-68b3ee138ac9" />

Note: I tried setting up the AWS Glue Crawler so that the data from the S3 bucket would be automatically converted to Athena tables; however, I encountered this access denied issue while setting up:
<img width="1236" height="254" alt="image" src="https://github.com/user-attachments/assets/c34dccfa-7461-4483-9ba8-43d128b13c14" />

- Next, created external tables manually in Athena DDL:
  - `flights` table
  - `users` table
<img width="1425" height="692" alt="image" src="https://github.com/user-attachments/assets/50b8bc1e-9946-44b8-b1e7-a49589950702" />

<img width="1420" height="685" alt="image" src="https://github.com/user-attachments/assets/2602c1b2-bafa-4105-8f84-a735c7a711ee" />

