import os

def walk_directory_tree(directory):
    """
    Walks through the directory tree starting from the given directory.
    Prints the directory path, subdirectories, and filenames.
    """
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f"Current Directory: {dirpath}")

        # Print the subdirectories in the current directory
        if dirnames:
            print("Subdirectories:")
            for dirname in dirnames:
                print(f" - {dirname}")

        # Print the files in the current directory
        if filenames:
            print("Files:")
            for filename in filenames:
                print(f" - {filename}")

        print("-" * 40)  # Separator for clarity


if __name__ == "__main__":
    # Define the directory you want to walk through
    directory_to_walk = "."  # You can replace this with any path, e.g., '/home/user/project'
    
    # Walk through the directory tree
    walk_directory_tree(directory_to_walk)
