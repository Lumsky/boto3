import boto3

ami_id = 'ami-01515c2704aa4c6bc'
key_pair_name = 'boto3-key-pair'
security_group_id = 'sg-054bbe8efed0dc6be'
ec2 = boto3.client('ec2')

response =ec2.run_instances(
    
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[security_group_id]
)

print(response["Instances"][0]["InstanceId"])