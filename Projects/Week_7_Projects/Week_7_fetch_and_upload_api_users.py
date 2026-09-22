import os
import csv
import json
import requests
import boto3
from dotenv import load_dotenv


load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION = os.getenv("AWS_DEFAULT_REGION", "ap-southeast-2")
BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME", "my-flight-pipeline-bucket")

def fetch_and_upload_users():
    print("Fetching users data from external API...")
    api_url = "https://jsonplaceholder.typicode.com/users"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        users = response.json()
        print(f"Successfully fetched {len(users)} users!")
        

        local_csv_path = "users_raw.csv"
        fieldnames = ["user_id", "name", "username", "email", "city"]
        
        with open(local_csv_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for u in users:
                writer.writerow({
                    "user_id": u["id"],
                    "name": u["name"],
                    "username": u["username"],
                    "email": u["email"],
                    "city": u["address"]["city"]
                })
                
        print("Converted API JSON to local CSV (users_raw.csv)...")
        

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=REGION
        )
        
        s3_key = "raw/users/users_raw.csv"
        s3_client.upload_file(local_csv_path, BUCKET_NAME, s3_key)
        
        print(f"Successfully uploaded users data to s3://{BUCKET_NAME}/{s3_key}")
        
    else:
        print(f"Failed to fetch API data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_and_upload_users()