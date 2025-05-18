import boto3

def create_instance(ec2, ami_id, security_group_id, key_pair_name, user_data=None):
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName=key_pair_name,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[security_group_id],
        UserData=user_data,
    )
    print(response["Instances"][0]["InstanceId"])

ami_id = 'ami-084568db4383264d4'
key_pair_name = 'boto3-key-pair'
security_group_id = 'sg-054bbe8efed0dc6be'

user_data = '''#!/bin/bash
    sudo apt-get update
    sudo apt-get install -y apache2
    sudo systemctl start apache2
    sudo systemctl enable apache2
    echo "<h1>Hello World!</h1>" | sudo tee /var/www/html/index.html
    '''

ec2 = boto3.client('ec2')
create_instance(ec2, ami_id, security_group_id, key_pair_name, user_data)
