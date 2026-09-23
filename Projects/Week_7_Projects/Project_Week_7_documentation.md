# Week 7 Project: Flight & Users Data Pipeline

## Project Overview
This project demonstrates the end-to-end cloud migration of a local data pipeline to AWS. The main objective is to ingest both static ([flights_raw.csv](https://github.com/btbarillo/DE_bootcamp3/tree/master/data/raw/flights_raw.csv)) and dynamic (https://jsonplaceholder.typicode.com/users) datasets, store them securely in Amazon S3, structure their schemas, and perform SQL-based data integration and analytics using Amazon Athena.


## Project Objective
To combine flight operational data with user profiles to identify which specific passengers (including their info such as cities and email addresses) are impacted by flight delays.


## Step-by-Step Implementation

### Step 1: Environment & Credentials setup
- Generated access keys on the AWS console for the `access key ID` and `secret access key`
- Created a `.env` file for AWS Credentials to ensure sensitive keys are not exposed. Note: This was not committed to the GitHub repo.

<img width="639" height="176" alt="image" src="https://github.com/user-attachments/assets/3920aa66-6874-45bf-8ab7-cb4c14e4d557" />

### Step 2: Data ingestion to Amazon S3
- Created and ran `Week_7_upload_csv_to_s3.py` to upload [flights_raw.csv](https://github.com/btbarillo/DE_bootcamp3/tree/master/data/raw/flights_raw.csv) to the AWS S3 bucket
- Created and ran  `Week_7_fetch_and_upload_api_users.py` to fetch from the API https://jsonplaceholder.typicode.com/users and convert the API JSON to a local CSV, then uploaded the local CSV to the AWS S3 bucket
<img width="1429" height="681" alt="image" src="https://github.com/user-attachments/assets/31801f8c-d480-4e64-b775-94d0bd24edfd" />
<img width="1148" height="436" alt="image" src="https://github.com/user-attachments/assets/5fb8a63c-cebb-4f9a-9782-d89c3664aee4" />
<img width="1134" height="454" alt="image" src="https://github.com/user-attachments/assets/01bb35a1-5829-4196-bf47-24f84bb0b3ee" />


### Step 3: Schema Creation in Amazon Athena
Note: I tried setting up the AWS Glue Crawler so that the data from the S3 bucket would be automatically converted to Athena tables; however, I encountered this access denied issue while setting up:
<img width="1236" height="254" alt="image" src="https://github.com/user-attachments/assets/c34dccfa-7461-4483-9ba8-43d128b13c14" />

- Due to permissions restrictions when setting up the AWS Glue Crawler, the `flight_delay_db` database was manually created in Athena DDL
<img width="1429" height="705" alt="image" src="https://github.com/user-attachments/assets/b892dc2e-7c42-4041-bd98-8a99fb240d78" />


- Next, created external tables manually in Athena DDL:
  - `flights` table
  - `users` table
<img width="1418" height="699" alt="image" src="https://github.com/user-attachments/assets/b3043c06-5ab0-43ed-a98d-9267d0573d7e" />
<img width="1433" height="693" alt="image" src="https://github.com/user-attachments/assets/3681a07b-a1eb-4f34-9bee-6cf05069bfbe" />


### Step 4: Data integration & Query analysis
- Performed an SQL JOIN to combine flight details with user profile data.

<img width="1427" height="691" alt="image" src="https://github.com/user-attachments/assets/73faab40-e64d-49f8-a62d-7c4dbd976435" />

```sql
WITH numbered_flights AS (
  SELECT 
    flight_id,
    airline,
    airport_code,
    delay_minutes,
    flight_date,
    ROW_NUMBER() OVER (ORDER BY flight_id) AS join_id
  FROM flight_delay_db.flights
),
numbered_users AS (
  SELECT 
    user_id,
    name,
    username,
    email,
    city,
    ROW_NUMBER() OVER (ORDER BY user_id) AS join_id
  FROM flight_delay_db.users
)
SELECT 
  f.flight_id,
  f.airline,
  f.airport_code,
  f.delay_minutes,
  f.flight_date,
  u.name AS passenger_name,
  u.email AS passenger_email,
  u.city AS passenger_city
FROM numbered_flights f
LEFT JOIN numbered_users u 
  ON f.join_id = u.join_id
ORDER BY f.delay_minutes DESC;
```
- The results were generated in the S3 bucket
<img width="1438" height="693" alt="image" src="https://github.com/user-attachments/assets/b52ea12d-0676-495d-a153-caaf1c3ec314" />
<img width="1434" height="692" alt="image" src="https://github.com/user-attachments/assets/eda57456-1e8a-47a5-8c82-3c47a9b325de" />
<img width="1425" height="697" alt="image" src="https://github.com/user-attachments/assets/16606de0-0b66-4166-ad54-78baa0ab39e7" />

Here's the CSV result: [Week_7_Project_Result.csv](https://github.com/btbarillo/DE_bootcamp3/blob/master/data/processed/Week_7_Project_Result.csv)
