import os

# 1. Get the current working directory
def get_current_working_directory():
    """Returns the current working directory using os.getcwd()"""
    return os.getcwd()

# 2. List files and directories in a specified directory
def list_directory_contents(path="."):
    """Returns a list of files and directories in the given path using os.listdir()"""
    try:
        return os.listdir(path)
    except FileNotFoundError:
        return f"Error: The directory {path} does not exist."

# 3. Check if a path is a file or a directory
def check_path_type(path):
    """Checks if the path is a file or directory using os.path.isfile() and os.path.isdir()"""
    if os.path.isfile(path):
        return f"{path} is a file."
    elif os.path.isdir(path):
        return f"{path} is a directory."
    else:
        return f"{path} does not exist."

# 4. Join two paths
def join_paths(base_path, relative_path):
    """Joins two paths using os.path.join()"""
    return os.path.join(base_path, relative_path)

# Main function to demonstrate the use of os module methods
if __name__ == "__main__":
    # 1. Get the current working directory
    current_dir = get_current_working_directory()
    print(f"Current Working Directory: {current_dir}")

    # 2. List the contents of the current directory
    directory_contents = list_directory_contents(current_dir)
    print(f"Contents of {current_dir}: {directory_contents}")

    # 3. Check if a given path is a file or a directory
    path_to_check = current_dir  # You can replace this with any path to check
    print(check_path_type(path_to_check))

    # 4. Join the current directory with a relative path (e.g., 'subdir')
    subdir = "subdir"  # Replace with an actual subdirectory or file in your environment
    joined_path = join_paths(current_dir, subdir)
    print(f"Joined Path: {joined_path}")

    # Check if the joined path exists
    print(check_path_type(joined_path))
