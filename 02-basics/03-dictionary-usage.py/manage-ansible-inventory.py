def ansible_inventory(inventory):
    for host, details in inventory.items():
        print(f"Host {host} (IP: {details['ip']}) is accessible via SSH key {details['ssh_key']}.")
    return inventory

# Dictionary representing Ansible inventory
inventory = {
    'webserver': {'ip': '192.168.1.10', 'ssh_key': '/home/user/.ssh/webserver_key'},
    'dbserver': {'ip': '192.168.1.20', 'ssh_key': '/home/user/.ssh/dbserver_key'},
    'loadbalancer': {'ip': '192.168.1.30', 'ssh_key': '/home/user/.ssh/lb_key'}
}

ansible_inventory(inventory)
