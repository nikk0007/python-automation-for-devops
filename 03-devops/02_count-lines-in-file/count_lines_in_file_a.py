import subprocess

# wc -l returnes one line less as it checks for newline character which might not be present after the last line.
result = subprocess.run(["cat sampleFile.txt | wc -l"], shell=True, capture_output=True, text=True)

print(result.stdout)
