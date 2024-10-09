from kubernetes import client, config

def create_deployment(name, namespace):
    # Load the kubeconfig file
    config.load_kube_config()

    # Define the container
    container = client.V1Container(
        name=name,
        image="nginx:latest",  # Replace with your desired image
        ports=[client.V1ContainerPort(container_port=80)]
    )

    # Create a Pod template
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": name}),
        spec=client.V1PodSpec(containers=[container])
    )

    # Create the Deployment spec
    deployment_spec = client.V1DeploymentSpec(
        replicas=2,
        template=template,
        selector={"matchLabels": {"app": name}}
    )

    # Create the Deployment
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=name),
        spec=deployment_spec
    )

    # Create the API client and create the deployment
    api_instance = client.AppsV1Api()
    api_instance.create_namespaced_deployment(namespace=namespace, body=deployment)
    print(f"Deployment '{name}' created in namespace '{namespace}'.")

if __name__ == "__main__":
    create_deployment("my-nginx", "default")  # Change namespace if needed
