import os
import boto3
from dotenv import load_dotenv

load_dotenv()

aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION', 'us-east-1')

glue = boto3.client(
    'glue',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

db_name = 'flight_delay_v2_db'
bucket_name = os.getenv("CLOUD_BUCKET_NAME", "my-flight-pipeline-bucket")

# --- 1. TABLE FOR AIRPORTS ---
airports_table = {
    'Name': 'airports',
    'Description': 'Airports metadata cataloged directly',
    'StorageDescriptor': {
        'Columns': [
            {'Name': 'faa', 'Type': 'string'},
            {'Name': 'name', 'Type': 'string'},
            {'Name': 'lat', 'Type': 'double'},
            {'Name': 'lon', 'Type': 'double'},
            {'Name': 'alt', 'Type': 'int'},
            {'Name': 'tz', 'Type': 'int'},
            {'Name': 'dst', 'Type': 'string'},
            {'Name': 'tzone', 'Type': 'string'}
        ],
        'Location': f"s3://{bucket_name}/raw/airports/",
        'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
        'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
        'SerdeInfo': {
            'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
            'Parameters': {'field.delim': ',', 'skip.header.line.count': '1'}
        }
    },
    'TableType': 'EXTERNAL_TABLE',
    'Parameters': {'classification': 'csv', 'typeOfData': 'file'}
}

# --- 2. TABLE FOR FLIGHTS ---
flights_table = {
    'Name': 'flights',
    'Description': 'Flight details dataset cataloged directly',
    'StorageDescriptor': {
        'Columns': [
            {'Name': 'year', 'Type': 'int'},
            {'Name': 'month', 'Type': 'int'},
            {'Name': 'day', 'Type': 'int'},
            {'Name': 'dep_time', 'Type': 'string'},
            {'Name': 'sched_dep_time', 'Type': 'string'},
            {'Name': 'dep_delay', 'Type': 'double'},
            {'Name': 'arr_time', 'Type': 'string'},
            {'Name': 'sched_arr_time', 'Type': 'string'},
            {'Name': 'arr_delay', 'Type': 'double'},
            {'Name': 'carrier', 'Type': 'string'},
            {'Name': 'flight', 'Type': 'string'},
            {'Name': 'tailnum', 'Type': 'string'},
            {'Name': 'origin', 'Type': 'string'},
            {'Name': 'dest', 'Type': 'string'},
            {'Name': 'air_time', 'Type': 'double'},
            {'Name': 'distance', 'Type': 'double'}
        ],
        'Location': f"s3://{bucket_name}/raw/flights/",
        'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
        'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
        'SerdeInfo': {
            'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
            'Parameters': {'field.delim': ',', 'skip.header.line.count': '1'}
        }
    },
    'TableType': 'EXTERNAL_TABLE',
    'Parameters': {'classification': 'csv', 'typeOfData': 'file'}
}

# Helper function para mag-create or update
def create_or_update_table(table_def):
    try:
        glue.create_table(DatabaseName=db_name, TableInput=table_def)
        print(f"🎉 Created table: {table_def['Name']}")
    except glue.exceptions.AlreadyExistsException:
        glue.update_table(DatabaseName=db_name, TableInput=table_def)
        print(f"🎉 Updated table: {table_def['Name']}")
    except Exception as e:
        print(f"Error for {table_def['Name']}: {e}")

# Execute both
create_or_update_table(airports_table)
create_or_update_table(flights_table)