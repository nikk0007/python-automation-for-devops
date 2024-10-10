# create a google form with the following fields:
Name: Short answer 
Employee Number: Short answer 
Phone: Short answer 
Address: Paragraph 
Designation: Short answer 
Technical Skills: Paragraph

# use the 3 dots on top right on google forms page to add Google Apps Script.

# create a Trigger:
Click on the clock icon (Triggers) in the toolbar. Then, click on + Add Trigger.
Select onFormSubmit from the Choose which function to run dropdown.
Select From form and On form submit from the respective dropdowns.
Click Save.

# lambda python code file name should be index.py.

# Zip it:
zip index.zip index.py

# Deploy Terraform script:
terraform apply -auto-approve
terraform destroy -auto-approve

# generate Lambda function URL from the AWS console and add it to the Google Apps script.

# remove any authentication to access Lambda. Make it publicly accessible for testing purposes. Also enable CORS.

# Now fill the google form and submit it. Its data will be sent to Lambda as payload and Lambda will put the data into the Employees dynamoDB table.