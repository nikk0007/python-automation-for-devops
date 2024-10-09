import boto3
import json

# Initialize a session using Amazon Lambda
client = boto3.client('lambda')

# Define IAM role for the Lambda function
iam_role = 'arn:aws:iam::123456789012:role/lambda-execution-role'  # Replace with your role ARN

# Read the zip file containing the Lambda function code
with open('function.zip', 'rb') as f:
    zipped_code = f.read()

# Create the Lambda function
response = client.create_function(
    FunctionName='HelloWorldFunction',
    Runtime='python3.8',  # Python version
    Role=iam_role,        # IAM role that Lambda assumes
    Handler='lambda_function.lambda_handler',  # The handler function in the lambda_function.py
    Code=dict(ZipFile=zipped_code),
    Description='A simple Hello World Lambda function',
    Timeout=15,  # Optional: Timeout in seconds
    MemorySize=128,  # Optional: Memory in MB
    Publish=True
)

# Print the Lambda function ARN
print(f"Lambda function ARN: {response['FunctionArn']}")
