function onFormSubmit(e) {
  // Log the entire event object to inspect what it contains
  Logger.log('Event Object: ' + JSON.stringify(e));
  
  if (e && e.values) {
    var formData = e.values;

    // Log the entire formData array to see what values it contains
    Logger.log('Form Data Array: ' + JSON.stringify(formData));

    // Access fields safely and log each field
    if (formData[1]) Logger.log('Name: ' + formData[1]);
    else Logger.log('Name field is undefined');
    
    if (formData[2]) Logger.log('Employee Number: ' + formData[2]);
    else Logger.log('Employee Number field is undefined');
    
    if (formData[3]) Logger.log('Phone: ' + formData[3]);
    else Logger.log('Phone field is undefined');
    
    if (formData[4]) Logger.log('Address: ' + formData[4]);
    else Logger.log('Address field is undefined');
    
    if (formData[5]) Logger.log('Designation: ' + formData[5]);
    else Logger.log('Designation field is undefined');
    
    if (formData[6]) Logger.log('Technical Skills: ' + formData[6]);
    else Logger.log('Technical Skills field is undefined');

    // Prepare the employee data object safely
    var employeeData = {
      "name": formData[1] || "",  // Safe access with fallback
      "employeeNumber": formData[2] || "",
      "phone": formData[3] || "",
      "address": formData[4] || "",
      "designation": formData[5] || "",
      "technicalSkills": formData[6] || ""
    };
    
    var payload = JSON.stringify(employeeData);

    var options = {
      'method': 'POST',
      'contentType': 'application/json',
      'payload': payload
    };

    try {
      // Call the AWS Lambda function URL
      var response = UrlFetchApp.fetch('https://tt7ksa7yzmc2zpbgvf6gwt2wyq0qhfsp.lambda-url.us-east-1.on.aws/', options);
      Logger.log('Response from Lambda: ' + response.getContentText());
    } catch (error) {
      Logger.log('Error calling Lambda: ' + error.message);
    }

  } else {
    Logger.log('Error: e.values is undefined');
  }
}

// Optional: This function installs the trigger for form submissions (if not set manually)
function installTrigger() {
  var form = FormApp.openById('16gd7Dlyy3DafZPShYuRxyYPiUOqB6e_mJouiyI6YjjI');  // Your Google Form ID
  ScriptApp.newTrigger('onFormSubmit')
    .forForm(form)
    .onFormSubmit()
    .create();
}
