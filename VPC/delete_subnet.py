import boto3

ec2 = boto3.client("ec2")


ec2.delete_subnet(
    SubnetId="subnet-0d55295b66dc78b89"
)