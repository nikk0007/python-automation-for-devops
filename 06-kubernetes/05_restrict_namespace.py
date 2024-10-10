from kubernetes import client, config
from kubernetes.client.exceptions import ApiException

# Function to list all namespaces
def list_namespaces():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    # Fetch all namespaces
    namespaces = v1.list_namespace().items
    return namespaces

# Function to check and add labels to the selected namespace
def add_labels_to_namespace(namespace):
    config.load_kube_config()
    v1 = client.CoreV1Api()

    # Define the labels to add
    labels_to_add = {
        "pod-security.kubernetes.io/enforce": "restricted",
        "pod-security.kubernetes.io/enforce-version": "latest"
    }

    try:
        # Get the current namespace details
        ns = v1.read_namespace(name=namespace)
        
        # Check if labels already exist
        existing_labels = ns.metadata.labels or {}
        labels_missing = {key: value for key, value in labels_to_add.items() if key not in existing_labels}

        if not labels_missing:
            print(f"All labels are already present in the namespace '{namespace}'.")
        else:
            # Add missing labels
            existing_labels.update(labels_missing)
            body = {
                "metadata": {
                    "labels": existing_labels
                }
            }

            # Update the namespace with new labels
            v1.patch_namespace(name=namespace, body=body)
            print(f"Added labels to namespace '{namespace}': {labels_missing}")
    
    except ApiException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Get the list of namespaces
    namespaces = list_namespaces()

    # Present the namespaces as a numbered list to the user
    print("Available Namespaces:")
    for i, ns in enumerate(namespaces, 1):
        print(f"{i}. {ns.metadata.name}")

    # Prompt the user to select a namespace
    choice = int(input("\nEnter the number of the namespace you want to select: ")) - 1
    selected_namespace = namespaces[choice].metadata.name

    # Check and add labels to the selected namespace
    add_labels_to_namespace(selected_namespace)
