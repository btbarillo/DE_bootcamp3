# Week 7 Project: Flight & Users Data Pipeline

## Project Overview
This project demonstrates the end-to-end cloud migration of a local data pipeline to AWS. The main objective is to ingest both static ([flights_raw.csv](https://github.com/btbarillo/DE_bootcamp3/tree/master/data/raw/flights_raw.csv)) and dynamic (https://jsonplaceholder.typicode.com/users) datasets, store them securely in Amazon S3, structure their schemas, and perform SQL-based data integration and analytics using Amazon Athena.


## Project Objective
To combine flight operational data with user profiles to identify which specific passengers(including their info such as cities and email addresses) are impacted by flight delays.


## Step-by-Step Implementation

### Step 1: Environment & Credentials Setup
- Created `.env` file for AWS Credentials to ensure sensitive keys are not exposed.

