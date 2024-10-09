def manage_kubernetes_pods(pods):
    for pod_name, config in pods.items():
        print(f"Pod {pod_name} runs {config['containers']} container(s) with {config['cpu_request']} CPU and {config['memory_limit']} memory limit.")
    return pods

# Dictionary representing pod configurations
pods = {
    'web-pod': {'containers': 2, 'cpu_request': '500m', 'memory_limit': '512Mi'},
    'db-pod': {'containers': 1, 'cpu_request': '1000m', 'memory_limit': '1Gi'},
    'cache-pod': {'containers': 1, 'cpu_request': '300m', 'memory_limit': '256Mi'}
}

manage_kubernetes_pods(pods)
