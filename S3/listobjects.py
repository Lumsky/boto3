import boto3

s3 = boto3.client("s3")

# response = s3.list_objects_v2(Bucket="lumi-boto3-1052025")

# for content in response["Contents"]:
#     print(content["Key"], content["LastModified"])

#searching a more limited info
# response = s3.list_objects_v2(Bucket="lumi-boto3-1052025", Prefix="test")

# for content in response["Contents"]:
#     print(content["Key"])


# def filter_objects_extension(client, bucket, extension):
#     """
#     List all objects in a bucket with a specific extension.
#     """
#     keys = []
#     response = client.list_objects_v2(Bucket=bucket)
#     for content in response["Contents"]:
#         if (extension in content["Key"][-(len(extension)):]):
#             keys.append(content["Key"]) 

#     return keys


def list_object_keys(client, bucket, prefix=""):
    """
    List all objects in a bucket with a specific extension.
    """
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response["Contents"]:
        keys.append(content["Key"]) 

    return keys

# if __name__ == "__main":
#     s3 = boto3.client("s3")

#     response = filter_objects_extension(s3, "lumi-boto3-1052025", ".txt")
#     print(response)
           
#     response = filter_objects_extension(s3, "lumi-boto3-1052025", ".txt")
#     print(response)

s3 = boto3.client("s3")
           
response = list_object_keys(s3, "lumi-boto3-1052025")
print(response)