
1. Create bucket

```
import boto3

# Initialize a session using Amazon S3
s3_client = boto3.client('s3')

# Define the bucket name (must be globally unique)
bucket_name = 'your-unique-bucket-name'

# Create the S3 bucket
response = s3_client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-3'
    }
)

# Print the response
print(response)

```

2. Copy local file:

```
import boto3

# Initialize a session using Amazon S3
s3_client = boto3.client('s3')

# Define the local file path and the S3 bucket name
local_file_path = 'path/to/your/local/file.txt'
bucket_name = 'your-bucket-name'
s3_object_key = 'folder-name/file.txt'  # Path in the S3 bucket

# Upload the file to the S3 bucket
s3_client.upload_file(local_file_path, bucket_name, s3_object_key)

print(f"File {local_file_path} uploaded to s3://{bucket_name}/{s3_object_key}")

```

3. remove file:

```
import boto3

# Initialize a session using Amazon S3
s3_client = boto3.client('s3')

# Define the S3 bucket name and the object key (file path in the bucket)
bucket_name = 'your-bucket-name'
s3_object_key = 'folder-name/file.txt'  # Path to the file in S3

# Delete the file from the S3 bucket
response = s3_client.delete_object(Bucket=bucket_name, Key=s3_object_key)

# Print the response to confirm the deletion
print(f"File {s3_object_key} deleted from bucket {bucket_name}")
```

4. romove bucket:

````
import boto3

# Initialize a session using Amazon S3
s3_client = boto3.client('s3')

# Define the S3 bucket name
bucket_name = 'your-bucket-name'

# First, delete all objects in the bucket (if necessary)
objects = s3_client.list_objects_v2(Bucket=bucket_name)

if 'Contents' in objects:
    for obj in objects['Contents']:
        s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
    print(f"All objects in the bucket {bucket_name} have been deleted.")

# Delete the S3 bucket
s3_client.delete_bucket(Bucket=bucket_name)

print(f"Bucket {bucket_name} has been deleted.")
```