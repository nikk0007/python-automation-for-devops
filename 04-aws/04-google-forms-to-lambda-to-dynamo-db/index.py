import json
import boto3
from botocore.exceptions import ClientError

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference to the DynamoDB table
table = dynamodb.Table('Employees')

def lambda_handler(event, context):
    try:
        # Parse the data from the incoming POST request body
        data = json.loads(event['body'])

        # Insert the parsed data into the DynamoDB table
        response = table.put_item(
            Item={
                'EmployeeNumber': data['employeeNumber'],  # Partition key
                'Name': data['name'],
                'Phone': data['phone'],
                'Address': data['address'],
                'Designation': data['designation'],
                'TechnicalSkills': data['technicalSkills']
            }
        )

        # Return a success response
        return {
            'statusCode': 200,
            'body': json.dumps('Employee info inserted successfully!')
        }

    except ClientError as e:
        # Return an error response if insertion fails
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error inserting data: {e.response['Error']['Message']}")
        }

    except Exception as e:
        # Catch any other exceptions and return an error response
        return {
            'statusCode': 500,
            'body': json.dumps(f"An unexpected error occurred: {str(e)}")
        }
