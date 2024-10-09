Prerequisites:
AWS Credentials: You must have your AWS credentials configured (either via AWS CLI or environment variables).
IAM Role: You need an IAM role with the appropriate permissions for Lambda and CloudWatch logging.

create a zip file of the lambda code:
zip function.zip lambda_function.py


Details:
client.create_function: Creates a new Lambda function.
FunctionName: The name of your Lambda function.
Runtime: The runtime environment for the Lambda function (e.g., Python 3.8).
Role: The ARN of the IAM role that the Lambda function assumes when it is invoked.
Handler: The handler function in your code (in this case, it's lambda_function.lambda_handler).
Code: The zip file containing the function code.
Timeout: The maximum time the Lambda function is allowed to run.
MemorySize: The amount of memory allocated to the function.