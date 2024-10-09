import json

def load_configuration(file_path):
    with open(file_path) as file:
        configuration = json.load(file)
    return configuration

def process_configuration(configuration):
    # Access and process specific configuration properties
    application_name = configuration['application_name']
    server_host = configuration['server']['host']
    server_port = configuration['server']['port']
    database_url = configuration['database']['url']
    # ... process other configuration properties

    # Print or perform further actions with the processed properties
    print("Application Name:", application_name)
    print("Server Host:", server_host)
    print("Server Port:", server_port)
    print("Database URL:", database_url)
    # ... perform other actions with the processed properties

# Example usage
config_file = 'sampleFile.json'  # Replace with your JSON configuration file path
config = load_configuration(config_file)
process_configuration(config)
