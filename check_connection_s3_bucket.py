import boto3
import sys

endpoint_url = ''
aws_access_key_id = ''
aws_secret_access_key = ''

s3_client = boto3.client(
    's3',
    endpoint_url=endpoint_url,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    use_ssl=True
    # region_name='us-east-1',  # You can specify any region
)

# Test the connection by listing buckets
response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
