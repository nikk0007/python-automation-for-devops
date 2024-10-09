# Function to demonstrate usage of List in DevOps (Example: Managing server IPs)
def manage_server_ips():
    # List of IP addresses of servers in a deployment
    server_ips = ['192.168.1.1', '192.168.1.2', '192.168.1.3']
    
    # Add a new server IP
    server_ips.append('192.168.1.4')
    
    # Remove a server IP that is decommissioned
    server_ips.remove('192.168.1.2')
    
    print("Updated server IP list:", server_ips)
    return server_ips

# Function to demonstrate usage of Tuple (Example: Immutable cloud instance configuration)
def cloud_instance_config():
    # Tuple representing cloud instance configuration (immutable)
    instance_config = ('t2.medium', 'us-west-2', 8, 16)  # (Instance Type, Region, vCPUs, Memory (GB))
    
    # Accessing values in tuple
    print(f"Instance Type: {instance_config[0]}, Region: {instance_config[1]}, vCPUs: {instance_config[2]}, Memory: {instance_config[3]} GB")

    return instance_config

# Function to demonstrate usage of Set (Example: Managing unique container images)
def manage_container_images():
    # Set of unique container images
    container_images = {'nginx:latest', 'redis:5', 'alpine:3.12'}
    
    # Add a new image
    container_images.add('nginx:1.19')
    
    # Check if an image exists
    if 'redis:5' in container_images:
        print("redis:5 is available.")
    
    # Remove an old image
    container_images.discard('alpine:3.12')
    
    print("Updated container images:", container_images)
    return container_images

# Function to demonstrate usage of Dictionary (Example: Managing cloud resource limits)
def manage_resource_limits():
    # Dictionary representing resource limits for Kubernetes namespaces
    resource_limits = {
        'namespace1': {'cpu': '500m', 'memory': '1Gi'},
        'namespace2': {'cpu': '1000m', 'memory': '2Gi'},
    }
    
    # Add a new namespace with resource limits
    resource_limits['namespace3'] = {'cpu': '750m', 'memory': '1.5Gi'}
    
    # Modify the resource limit for an existing namespace
    resource_limits['namespace1']['memory'] = '2Gi'
    
    # Iterate over the dictionary to display limits
    for namespace, limits in resource_limits.items():
        print(f"{namespace} -> CPU: {limits['cpu']}, Memory: {limits['memory']}")
    
    return resource_limits

# Call the methods to demonstrate their usage
if __name__ == "__main__":
    manage_server_ips()
    cloud_instance_config()
    manage_container_images()
    manage_resource_limits()

print(f"__name__ = {__name__}")
# manage_server_ips()
# cloud_instance_config()
# manage_container_images()
# manage_resource_limits()