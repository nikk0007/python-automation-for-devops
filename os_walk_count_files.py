import os

def count_py_files(directory):
    """Counts the total number of .py files in the given directory and its subdirectories."""
    py_file_count = 0
    
    # Use os.walk() to traverse the directory tree
    for root, dirs, files in os.walk(directory):
        # Loop through the files in the current directory
        for file in files:
            # Check if the file has a .py extension
            if file.endswith('.py'):
                print(file)
                py_file_count += 1
    
    return py_file_count

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    total_py_files = count_py_files(current_directory)
    
    print(f"Total number of .py files in '{current_directory}': {total_py_files}")
