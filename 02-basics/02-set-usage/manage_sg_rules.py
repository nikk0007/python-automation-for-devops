def manage_security_group_rules(current_rules, desired_rules):
    # Convert inbound IP addresses to sets for comparison
    current_ips = set(current_rules['allowed_ips'])
    desired_ips = set(desired_rules['allowed_ips'])

    # Find missing IPs in current rules that should be allowed
    missing_ips = desired_ips - current_ips
    # Find extra IPs in current rules that shouldn't be allowed
    extra_ips = current_ips - desired_ips

    print(f"IPs missing in current rules: {missing_ips}")
    print(f"Extra IPs in current rules: {extra_ips}")
    return missing_ips, extra_ips

# Example current and desired security group rules
current_rules = {'allowed_ips': ['192.168.1.10', '10.0.0.1', '172.16.0.5']}
desired_rules = {'allowed_ips': ['192.168.1.10', '10.0.0.2', '172.16.0.5']}

manage_security_group_rules(current_rules, desired_rules)
