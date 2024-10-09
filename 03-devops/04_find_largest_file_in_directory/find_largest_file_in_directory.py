import os

def find_largest_file(directory):
    max_size = 0
    largest_file = None

    for base_path, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(base_path, file)
            file_size = os.path.getsize(file_path)
            if file_size > max_size:
                max_size = file_size
                largest_file = file_path

    return largest_file, max_size

# Example usage
directory_path = 'myfiles'
largest_file, size = find_largest_file(directory_path)
if largest_file:
    print(f"The largest file in '{directory_path}' is '{largest_file}' with size {size} bytes.")
else:
    print(f"No files found in '{directory_path}'.")
