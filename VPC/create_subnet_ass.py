import boto3

vpc_id = "vpc-0815091417e6de3b5"
route_table_id = "rtb-071b612ac07fab084"
subnet_id = "subnet-0d55295b66dc78b89"

ec2 = boto3.client("ec2")



subnet_association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id
)

print(subnet_association["AssociationId"])