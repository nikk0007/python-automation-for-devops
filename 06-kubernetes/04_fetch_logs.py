from kubernetes import client, config

def fetch_logs(namespace, pod_name):
    # Load the kubeconfig file
    config.load_kube_config()

    # Create an API client
    api_instance = client.CoreV1Api()

    # Fetch the logs from the specified pod
    logs = api_instance.read_namespaced_pod_log(name=pod_name, namespace=namespace)
    print(f"Logs from pod '{pod_name}':\n{logs}")

if __name__ == "__main__":
    fetch_logs("default", "my-nginx-74d7fb65c9-8gxnf")  # Replace with your pod name
