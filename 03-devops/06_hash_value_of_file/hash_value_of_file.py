import hashlib

# MD5 is another hash_algorithm which can also be used
def calculate_file_hash(file_path, hash_algorithm='sha256'):
    """
    Calculates the hash value of a file using the specified hash algorithm.
    
    Args:
        file_path (str): The path to the file.
        hash_algorithm (str): The hash algorithm to use (default: 'sha256').
    
    Returns:
        str: The hash value of the file.
    """
    hash_object = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        # Read the file in chunks to avoid loading the entire file into memory
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)
    return hash_object.hexdigest()

# Example usage
file_path = 'sampleFile.txt'
hash_value = calculate_file_hash(file_path)
print(f"The hash value of {file_path} is: {hash_value}")
