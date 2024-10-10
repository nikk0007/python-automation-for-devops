import requests

# GET request
response = requests.get('https://reqres.in/api/users?page=2')
if response.status_code == 200:
    data = response.json()
    # Process the JSON data returned from the API
    print(data)
    print("\n")
else:
    print('Error:', response.status_code)

# POST request
payload = {
    "name": "morpheus",
    "job": "leader"
}
response = requests.post('https://reqres.in/api/users', json=payload)
if response.status_code == 201:
    data = response.json()
    # Process the JSON data returned from the API
    print(data)
    print("\n")
else:
    print('Error:', response.status_code)

# PUT request
payload = {
    "name": "morpheus",
    "job": "zion resident"
}
response = requests.put('https://reqres.in/api/users/2', json=payload)
if response.status_code == 200:
    data = response.json()
    # Process the JSON data returned from the API
    print(data)
    print("\n")
else:
    print('Error:', response.status_code)
\
# DELETE request
response = requests.delete('https://reqres.in/api/users/2')
if response.status_code == 204:
    print('User deleted successfully')
    print("\n")
else:
    print('Error:', response.status_code)