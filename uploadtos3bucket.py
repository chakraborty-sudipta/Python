import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Step 1: Initialize the S3 client
s3_client = boto3.client('s3')

# Step 2: Define the bucket name and the file to upload
bucket_name = 'my-img-bucket-2024'  # Replace with your bucket name
file_name = '/home/sudipta/Python/sambit.jpg'  # Replace with the path to your file
object_name = 'sambit.jpg'  # Name to give the file in S3

# Step 3: Upload the file
try:
    s3_client.upload_file(file_name, bucket_name, object_name)
    print(f"'{file_name}' has been uploaded to '{bucket_name}/{object_name}'")
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except NoCredentialsError:
    print("Credentials not available.")
except PartialCredentialsError:
    print("Incomplete credentials provided.")
except Exception as e:
    print(f"An error occurred: {e}")