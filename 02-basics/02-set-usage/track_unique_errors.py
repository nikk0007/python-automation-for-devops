def track_unique_errors(logs):
    # Set to track unique error messages
    unique_errors = set()

    for log in logs:
        if log['level'] == 'error':
            unique_errors.add(log['message'])
    
    print(f"Unique errors encountered: {unique_errors}")
    return unique_errors

# Example logs
logs = [
    {'level': 'info', 'message': 'Service started'},
    {'level': 'error', 'message': 'Database connection failed'},
    {'level': 'error', 'message': 'Timeout occurred'},
    {'level': 'error', 'message': 'Database connection failed'},  # Duplicate error
]

track_unique_errors(logs)
