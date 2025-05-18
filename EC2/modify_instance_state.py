import boto3

InstanceIds = ['i-02ca13912e3641830', 'i-064831d1e09e0f993', 'i-09f99e41ba7ddf973']


for instance in InstanceIds:

    def stop_instance(client, instance_id):
        response = client.stop_instances(
            InstanceIds=[
            instance_id,
            ],
        )
        print('Stopping instance:', instance_id)


    def start_instance(client, instance_id):
        response = client.start_instances(
            InstanceIds=[
            instance_id,
            ],
        )
        print('Starting instance:', instance_id)


    def terminate_instance(client, instance_id):
        response = client.terminate_instances(
            InstanceIds=[
            instance_id,
            ],
        )
        print('Terminating instance:', instance_id)


    if __name__ == "__main__":
        instance_id = InstanceIds[1]
        ec2 = boto3.client('ec2')
        terminate_instance(ec2, instance_id)
    

