import os
from pathlib import Path
import boto3
from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = os.getenv("CLOUD_BUCKET_NAME", "my-flight-pipeline-bucket")
AWS_REGION = os.getenv("AWS_REGION", "ap-southeast-2")

CURRENT_FILE = Path(__file__).resolve()
ROOT_DIR = CURRENT_FILE.parents[2] 
DATA_DIR = ROOT_DIR / "data" / "raw"

FILES_TO_UPLOAD={
    "flights_raw.csv": "raw/flights/flights_raw.csv",
    "airports_lookup.csv": "raw/airports/airports_lookup.csv",
}

def upload_files_to_s3():
    print(f"Target S3 Bucket: {BUCKET_NAME}")
    print(f"Looking for raw files in: {DATA_DIR.resolve()}")

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=AWS_REGION
    )

    for local_filename, s3_key in FILES_TO_UPLOAD.items():
        local_path = DATA_DIR / local_filename

        if not local_path.exists():
            print(f"File not found at: {local_path}")
            continue 

        try:
            print(f"Uploading {local_filename} -> s3://{BUCKET_NAME}/{s3_key}...")
            s3_client.upload_file(str(local_path), BUCKET_NAME, s3_key)
            print(f"Successfully uploaded {local_filename}!")
        except Exception as e:
            print(f"Failed to upload {local_filename}: {e}")


if __name__ == "__main__":
    upload_files_to_s3()