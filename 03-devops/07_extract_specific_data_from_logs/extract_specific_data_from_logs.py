import re

def extract_error_messages(file_path):
    error_messages = []
    
    with open(file_path, 'r') as log_file:
        for line in log_file:
            match = re.search(r'ERROR: (.+)', line)
            if match:
                #error_messages.append(match.group(1))
                error_messages.append(line)
    
    return error_messages

# Example usage
log_file_path = 'sampleFile.txt'
errors = extract_error_messages(log_file_path)

# Print the extracted error messages
for error in errors:
    print(error)
