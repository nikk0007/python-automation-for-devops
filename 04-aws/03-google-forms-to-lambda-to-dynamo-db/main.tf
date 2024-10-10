provider "aws" {
  region = "us-east-1"
}

resource "aws_dynamodb_table" "employees" {
  name           = "Employees"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "EmployeeNumber"
  attribute {
    name = "EmployeeNumber"
    type = "S"
  }
}

resource "aws_iam_role" "lambda_execution_role" {
  name = "lambda_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_policy_attachment" "lambda_execution_policy" {
  name       = "lambda_execution_policy"
  roles      = [aws_iam_role.lambda_execution_role.name]
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy" "dynamodb_policy" {
  name = "dynamodb_policy"
  role = aws_iam_role.lambda_execution_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "dynamodb:PutItem",
          "dynamodb:UpdateItem",
          "dynamodb:DeleteItem"
        ]
        Resource = "*"
      }
    ]
  })
}

resource "aws_lambda_function" "form_submission_lambda" {
  function_name = "form_submission_lambda"
  handler       = "index.lambda_handler"
  role          = aws_iam_role.lambda_execution_role.arn
  runtime       = "python3.8"

  filename         = "index.zip"
  source_code_hash = filebase64sha256("index.zip")

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.employees.name
    }
  }
}

resource "aws_lambda_permission" "allow_invoke" {
  statement_id  = "AllowExecutionFromAPI"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.form_submission_lambda.function_name
  principal     = "apigateway.amazonaws.com"
}

output "lambda_url" {
  value = aws_lambda_function.form_submission_lambda.invoke_arn
}
