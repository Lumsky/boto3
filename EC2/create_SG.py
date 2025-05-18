import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='SG from boto3',
    GroupName='boto3-SG',
    VpcId='vpc-089028aa5fdacf5f7',
)

print(response['GroupId'])

