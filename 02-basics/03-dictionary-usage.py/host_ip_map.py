def resolve_hostnames_to_ips(hosts):
    for hostname, ip in hosts.items():
        print(f"{hostname} resolves to {ip}")
    return hosts

# Dictionary mapping hostnames to IPs
hosts = {
    'webserver': '192.168.1.10',
    'dbserver': '192.168.1.20',
    'cache': '192.168.1.30'
}

resolve_hostnames_to_ips(hosts)
