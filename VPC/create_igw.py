import boto3

ec2 = boto3.client("ec2")

# igw = ec2.create_internet_gateway()

# print(igw["InternetGateway"]["InternetGatewayId"])


# Attach the Internet Gateway to a VPC
vpc_id = "vpc-0815091417e6de3b5"
igw_id = "igw-096ec488696ef898a"

attachment = ec2.attach_internet_gateway(
    InternetGatewayId=igw_id,
    VpcId=vpc_id
)       
