from kubernetes import client, config

def list_pods(namespace):
    # Load the kubeconfig file
    config.load_kube_config()

    # Create an API client
    api_instance = client.CoreV1Api()

    # List pods in the specified namespace
    pods = api_instance.list_namespaced_pod(namespace)
    for pod in pods.items:
        print(f"Pod Name: {pod.metadata.name}, Status: {pod.status.phase}")

if __name__ == "__main__":
    list_pods("default")  # Change namespace if needed
