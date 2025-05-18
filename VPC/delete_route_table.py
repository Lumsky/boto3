import boto3

ec2 = boto3.client("ec2")

ec2.delete_route_table(
    RouteTableId="rtb-06b0c70acf83e66b9"
)   