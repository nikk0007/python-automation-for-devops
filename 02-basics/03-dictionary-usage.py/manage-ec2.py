def manage_ec2_metadata(instances):
    for instance_id, metadata in instances.items():
        print(f"Instance {instance_id} is of type {metadata['instance_type']} in {metadata['region']} region and is currently {metadata['state']}.")
    return instances

# Dictionary of EC2 instance metadata
instances = {
    'i-001': {'instance_type': 't2.micro', 'region': 'us-east-1', 'state': 'running'},
    'i-002': {'instance_type': 't2.medium', 'region': 'us-west-2', 'state': 'stopped'},
    'i-003': {'instance_type': 't3.large', 'region': 'eu-central-1', 'state': 'terminated'}
}

manage_ec2_metadata(instances)
