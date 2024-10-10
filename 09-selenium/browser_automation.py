from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (ensure the correct path to your WebDriver)
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# Open the form URL
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSflJacXGAJk0hb9_HlOrFNOJsw5wIBpBhP7J4xGHwYJRZFm4Q/viewform")

# WebDriverWait with 10-second timeout
wait = WebDriverWait(driver, 10)

# Fill the 'Name' field
name_field = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-labelledby='i1']"))
)
name_field.send_keys("Niket Singh")

# Fill the 'Employee Number' field
employee_number_field = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-labelledby='i5']"))
)
employee_number_field.send_keys("12345")

# Fill the 'Phone' field
phone_field = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-labelledby='i9']"))
)
phone_field.send_keys("9650311070")

# Fill the 'Address' field
address_field = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-labelledby='i13']"))
)
address_field.send_keys("123, Sample Street, Gurgaon")

# Fill the 'Designation' field
designation_field = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-labelledby='i17']"))
)
designation_field.send_keys("Devops Engineer")

# Fill the 'Technical Skills' field
skills_field = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-labelledby='i21']"))
)
skills_field.send_keys("Python, DevOps, Kubernetes, AWS")

# Locate the submit button and click it
submit_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and contains(text(), 'Submit')]"))
)
submit_button.click()

# Close the browser
driver.quit()
