from kubernetes import client, config

def scale_deployment(name, namespace, replicas):
    # Load the kubeconfig file
    config.load_kube_config()

    # Create an API client
    api_instance = client.AppsV1Api()

    # Fetch the deployment
    deployment = api_instance.read_namespaced_deployment(name=name, namespace=namespace)

    # Update the number of replicas
    deployment.spec.replicas = replicas

    # Scale the deployment
    api_instance.patch_namespaced_deployment(name=name, namespace=namespace, body=deployment)
    print(f"Scaled deployment '{name}' to {replicas} replicas in namespace '{namespace}'.")

if __name__ == "__main__":
    scale_deployment("my-nginx", "default", 3)  # Change namespace and replicas as needed
