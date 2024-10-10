import paramiko

def execute_commands(ssh_client, commands):
    """Execute a list of commands on the remote server."""
    for command in commands:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        stdin.write('your_sudo_password\n')  # Provide the password for sudo if required
        stdin.flush()
        print(f"Executing: {command}")
        print(stdout.read().decode())
        print(stderr.read().decode())

def main():
    # Remote server details
    remote_ip = '54.198.171.161'  # Replace with your EC2 instance public IP
    remote_user = 'ubuntu'  # Change if necessary
    private_key_path = './mykey'  # Path to your private key

    # Commands to be executed
    commands = [
        "sudo apt update",  # Update package list
        "sudo apt install -y unzip",  # Install unzip package
        "cd /var/www/html/",
        "sudo wget https://www.tooplate.com/zip-templates/2125_artxibition.zip",
        "sudo unzip -o 2125_artxibition.zip",  # Unzip directly into the current directory
        "sudo rm index.nginx-debian.html",  # Delete the original index file
        "sudo mv 2125_artxibition/* /var/www/html/",  # Move contents to /var/www/html/
        "sudo rm -rf 2125_artxibition",  # Remove the directory created after unzip
        "sudo rm 2125_artxibition.zip",  # Optionally delete the zip file
        "sudo systemctl restart nginx"  # Restart Nginx server
    ]

    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Load the private key
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
    
    try:
        # Connect to the remote server
        ssh_client.connect(remote_ip, username=remote_user, pkey=private_key)
        print(f"Connected to {remote_ip}")

        # Execute the commands
        execute_commands(ssh_client, commands)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the SSH connection
        ssh_client.close()

if __name__ == "__main__":
    main()
