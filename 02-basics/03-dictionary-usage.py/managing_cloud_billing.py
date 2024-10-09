def calculate_cloud_costs(cost_data):
    total_cost = 0
    for region, services in cost_data.items():
        region_cost = sum(services.values())
        print(f"Total cost in {region}: ${region_cost}")
        total_cost += region_cost
    
    print(f"Total cloud cost: ${total_cost}")
    return total_cost

# Dictionary storing cloud cost data
cost_data = {
    'us-east-1': {'EC2': 120.5, 'S3': 45.3, 'RDS': 65.8},
    'us-west-2': {'EC2': 140.7, 'S3': 50.1, 'RDS': 70.0},
    'eu-central-1': {'EC2': 130.4, 'S3': 47.9, 'RDS': 60.6}
}

calculate_cloud_costs(cost_data)
