import boto3
from listobjects import list_object_keys

# s3 = boto3.client("s3")
# bucket = 'lumi-boto3-1052025'
# key = 'test_upload.txt'

#response = s3.get_object(Bucket=bucket, Key=key)
# object_content = response['Body'].read()
# contents = object_content.decode("utf-8")

# print(contents)

#deleting one object using boto3
# response = s3.delete_object(
#     Bucket=bucket, 
#     Key=key)
#print("Object deleted")

#deleting multiple objects using boto3

def delete_object(client, bucket, key):
    """
    Delete multiple objects from a bucket.
    """
    response = client.delete_objects(
        Bucket=bucket,
        Key=key)
    return response


def delete_objects(client, bucket, keys):
    """
    Delete multiple objects from a bucket.
    """
    objects = [{'Key': key} for key in keys]
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects,       
        }
    )
    return response

if __name__ == "__main__":
    bucket = 'lumi-boto3-1052025'
    s3 = boto3.client("s3")

    prefix = "folder/folders/"

    keys = list_object_keys(s3, bucket, prefix=prefix)
    print(keys)
    keys = [key for key in keys if "/" in key[len(prefix):]]
    print(keys)
    delete_objects(s3, bucket, keys)

def delete_objects_non_recursive(client, bucket, keys, prefix):
    keys = [key for key in keys if "/" not in key[len(prefix):]]
    objects = [{'Key': key} for key in keys]

    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects,       
        }
    )
    return response

if __name__ == "__main__":
    bucket = 'lumi-boto3-1052025'
    s3 = boto3.client("s3")

    prefix = "folder/folders/"

    keys = list_object_keys(s3, bucket, prefix=prefix)
    keys = [key for key in keys if "/" not in key[len(prefix):]]
    delete_objects_non_recursive(s3, bucket, keys, prefix)