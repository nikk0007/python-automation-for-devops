import os
import re

def search_files(directory, pattern, search_string):
    matches = []
    regex = re.compile(pattern)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                contents = f.read()
                if regex.search(contents) and search_string in contents:
                    matches.append(file_path)

    return matches

# Example usage
directory = 'path/to/directory'  # Specify the directory to search in
pattern = r'\.txt$'  # Specify the file pattern using a regular expression
search_string = 'example'  # Specify the string to search for

results = search_files(directory, pattern, search_string)
if results:
    print("Found matches in the following files:")
    for file in results:
        print(file)
else:
    print("No matches found.")
