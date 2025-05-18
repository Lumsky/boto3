import boto3

s3 = boto3.client("s3")

#You can use this URL to download the object from S3 without needing to authenticate with AWS credentials.
# The URL will expire after 300 seconds (5 minutes) and will no longer be valid.
response = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': "lumi-boto3-1052025", 
                    'Key': "test3.txt"},
            ExpiresIn=300
        )
print(response)
