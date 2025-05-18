import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_route_tables()

for route_table in response["RouteTables"]:
    print(route_table["RouteTableId"],
          route_table["VpcId"]
          )

    for association in route_table["Associations"]:
        print(association["RouteTableAssociationId"],
              )
        if "subnet_id" in association: 
            print("subnet_id")

    for route in route_table["Routes"]:
        print(route["DestinationCidrBlock"],
              route["GatewayId"]
              )