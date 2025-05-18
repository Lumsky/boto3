import boto3
import os
from listobjects import list_objects_keys

def download_single_object(s3, bucket, key, filename):
    # Download a single object
    s3.download_file(bucket, key, filename)
    print("Download complete")


if __name__ == "__main":

    bucket = 'lumi-boto3-1052025'   
    key = 'test3.txt'
    filename = 'test3.txt'

    s3 = boto3.client("s3")

    keys = list_objects_keys(s3, bucket, prefix="folder/ ")

    for key in keys:
        if '/' ==  key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        else:
            download_single_object(s3, bucket, key, key)