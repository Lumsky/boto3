import boto3

route_table_id = "rtb-071b612ac07fab084"
vpc_id = "vpc-0815091417e6de3b5"
igw_id = "igw-096ec488696ef898a"

ec2 = boto3.client("ec2")

ec2.create_route(
    DestinationCidrBlock="0.0.0.0/0",
    GatewayId=igw_id,
    RouteTableId=route_table_id
)
