import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId='ami-053b0d53c279acc90',
    InstanceType='t2.micro',
    MinCount=2,
    MaxCount=2
)

# Print the details of each EC2 instance
for instance in instances:
    print("Instance ID:", instance.id)
    print("State:", instance.state['Name'])
    print("Public IP:", instance.public_ip_address)
    print("Private IP:", instance.private_ip_address)
    print("Instance Type:", instance.instance_type)
    print("-----")

