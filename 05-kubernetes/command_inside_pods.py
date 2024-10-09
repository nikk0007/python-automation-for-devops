from kubernetes import client, config
from kubernetes.stream import stream

def exec_command_in_pod(namespace, pod_name, command):
    # Load the kubeconfig file
    config.load_kube_config()

    # Create an API client
    api_instance = client.CoreV1Api()

    # Prepare the exec command
    exec_command = [
        '/bin/sh',
        '-c',
        command
    ]

    # Execute the command in the pod
    response = stream(api_instance.connect_get_namespaced_pod_exec,
                      pod_name,
                      namespace,
                      command=exec_command,
                      stderr=True, 
                      stdin=False,
                      stdout=True,
                      tty=False)

    print(f"Command output: {response}")

if __name__ == "__main__":
    exec_command_in_pod("default", "my-nginx-74d7fb65c9-bn8dw", "ls /")  # Replace with your pod name and command
