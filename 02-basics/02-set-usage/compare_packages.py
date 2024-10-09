def compare_installed_packages(server1, server2):
    # Using sets to store unique installed packages
    server1_packages = set(server1['packages'])
    server2_packages = set(server2['packages'])

    # Find packages that are in server1 but not in server2
    missing_in_server2 = server1_packages - server2_packages
    # Find packages that are in server2 but not in server1
    missing_in_server1 = server2_packages - server1_packages

    print(f"Packages missing in Server 2: {missing_in_server2}")
    print(f"Packages missing in Server 1: {missing_in_server1}")
    return missing_in_server2, missing_in_server1

# Example installed packages on two servers
server1 = {'id': 'server1', 'packages': ['nginx', 'mysql', 'python', 'git']}
server2 = {'id': 'server2', 'packages': ['nginx', 'python', 'git', 'docker']}

compare_installed_packages(server1, server2)
