def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            empty_lines = 0
            comment_lines = 0
            for line in file:
                line_count += 1
                if line.strip() == "":
                    empty_lines += 1
                if line.strip().startswith("#"):
                    comment_lines += 1
        return line_count, empty_lines, comment_lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return -1, -1, -1

# Example usage
file_path = 'sampleFile.txt'
lines, empty, comments = count_lines(file_path)
if lines >= 0:
    print(f"The file '{file_path}' contains {lines} lines.")
    print(f"Empty lines: {empty}")
    print(f"Comment lines: {comments}")
