import sys
from datetime import datetime, timezone, timedelta
from io import StringIO
from google.cloud import storage
from pyspark.sql import SparkSession

def get_latest_gcs_subfolder(bucket_name, prefix):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = list(client.list_blobs(bucket_name, prefix=prefix))
    
    subfolders = set()
    for blob in blobs:
        rel_path = blob.name[len(prefix):].lstrip('/')
        parts = rel_path.split('/')
        if len(parts) > 1 and parts[0]:
            subfolders.add(parts[0])
            
    if not subfolders:
        raise ValueError(f"No subfolders found under gs://{bucket_name}/{prefix}")
    
    latest_folder = sorted(list(subfolders))[-1]
    return latest_folder

spark = SparkSession.builder \
    .appName("UserCountriesETL") \
    .getOrCreate()

bucket_name = "berns-earthquake-pipeline-gcp"
prefix = "raw/users/"

if len(sys.argv) > 1 and sys.argv[1] != "*":
    target_folder = sys.argv[1]
    print(f"Using provided subfolder argument: {target_folder}")
else:
    target_folder = get_latest_gcs_subfolder(bucket_name, prefix)
    print(f"Auto-detected latest subfolder: {target_folder}")

input_path = f"gs://{bucket_name}/{prefix}{target_folder}/*.csv"
print(f"Reading CSV files from: {input_path}")

df_spark = spark.read.option("header", "true").csv(input_path)


df_pd = df_spark.toPandas()

ph_time = datetime.now(timezone.utc) + timedelta(hours=8)
execution_date = ph_time.strftime("%Y-%m-%d")


output_key = f"processed/users/dt={execution_date}/user_countries_clean.csv"

csv_buffer = StringIO()
df_pd.to_csv(csv_buffer, index=False)

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(output_key)
blob.upload_from_string(csv_buffer.getvalue(), content_type="text/csv")

print(f"Successfully saved clean CSV to: gs://{bucket_name}/{output_key}")
spark.stop()