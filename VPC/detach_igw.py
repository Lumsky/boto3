import boto3

ec2 = boto3.client("ec2")
vpc_id = "vpc-0815091417e6de3b5"
igw_id = "igw-096ec488696ef898a"

ec2.detach_internet_gateway(
    InternetGatewayId=igw_id,
    VpcId=vpc_id
)

