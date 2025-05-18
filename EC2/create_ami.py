import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-080d48e6e45c7ff2a',
    Name='server1'
)       

for image in response["Images"]:
    print(image['ImageId'], image['CreationDate'], image['Name'])
