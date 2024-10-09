import os
import glob

def delete_oldest_file(directory):
    # Get a list of all files in the directory
    files = glob.glob(os.path.join(directory, "*"))

    if not files:
        print("Directory is empty. No files to delete.")
        return

    # Sort the files by modification time (oldest first)
    files.sort(key=lambda x: os.path.getmtime(x))

    # Delete the oldest file
    oldest_file = files[0]
    os.remove(oldest_file)
    print(f"Deleted file: {oldest_file}")

# Specify the directory path
directory_path = "mydir"

# Call the function
delete_oldest_file(directory_path)
