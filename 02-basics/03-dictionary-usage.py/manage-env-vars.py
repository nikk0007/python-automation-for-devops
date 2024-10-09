import os

def manage_env_vars():
    env_vars = {
        'AWS_ACCESS_KEY': os.getenv('AWS_ACCESS_KEY'),
        'AWS_SECRET_KEY': os.getenv('AWS_SECRET_KEY'),
        'REGION': os.getenv('AWS_REGION', 'us-east-1'),  # Default to us-east-1 if not set
    }

    for var, value in env_vars.items():
        print(f"{var} = {value}")
    return env_vars

manage_env_vars()
