import boto3

s3 = boto3.client("s3")

#create a bucket
# response = s3.create_bucket(
#     Bucket='lumi-boto3-1052025')
# print(response)


#list all buckets
# response = s3.list_buckets()
# buckets = response["Buckets"]
# for bucket in buckets:
#     print(bucket["Name"], bucket["CreationDate"])

#upload an existing file to a bucket using boto3
# with open("test.txt", "rb") as f:
#     s3.put_object(
#         Bucket="lumi-boto3-1052025",
#         Key="test.txt",
#         Body=f,
#         ContentType="text/plain"
# )   
#another way to upload a file to a bucket using boto3
# s3.upload_file("test.txt", "lumi-boto3-1052025", "test_upload.txt", 
#                ExtraArgs={"ContentType": "text/plain"})    

#uplaod a new object to a bucket using boto3
s3.put_object(
    Bucket="lumi-boto3-1052025",
    Key="folder/folders/fodler1/test3.txt",
    Body="Hello World, this is a test file",
    ContentType="text/plain"
)

