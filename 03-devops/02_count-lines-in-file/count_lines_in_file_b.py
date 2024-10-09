def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return -1

# Example usage
file_path = 'sampleFile.txt'
lines = count_lines(file_path)
if lines >= 0:
    print(f"The file '{file_path}' contains {lines} lines.")
