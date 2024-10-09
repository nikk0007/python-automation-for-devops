def track_container_images(pods):
    # Set to store unique container images
    container_images = set()

    for pod in pods:
        for container in pod['containers']:
            container_images.add(container['image'])
    
    print(f"Unique container images in use: {container_images}")
    return container_images

# Example list of pods with container images
pods = [
    {'name': 'web-pod', 'containers': [{'name': 'nginx', 'image': 'nginx:1.19'}, {'name': 'redis', 'image': 'redis:5.0'}]},
    {'name': 'db-pod', 'containers': [{'name': 'mysql', 'image': 'mysql:8.0'}]},
    {'name': 'web-pod', 'containers': [{'name': 'nginx', 'image': 'nginx:1.19'}]}  # Duplicate image
]

track_container_images(pods)
