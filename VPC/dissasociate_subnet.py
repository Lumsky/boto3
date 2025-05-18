import boto3

route_table_id = "rtb-071b612ac07fab084"

ec2 = boto3.client("ec2")

response = ec2.describe_route_tables(
    RouteTableIds=[route_table_id]
    )

for association in response["RouteTables"][0]["Associations"]:
    if not association["Main"]:
        AssociationId=association["RouteTableAssociationId"]
        print(AssociationId)
        ec2.disassociate_route_table(
            AssociationId=AssociationId
        )
        