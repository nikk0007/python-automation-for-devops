import requests

# GET request
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
if response.status_code == 200:
    data = response.json()
    # Process the JSON data returned from the API
    print(data)
else:
    print('Error:', response.status_code)

# POST request
payload = {'name': 'John', 'email': 'john@example.com'}
response = requests.post('https://api.example.com/users', json=payload)
if response.status_code == 201:
    data = response.json()
    # Process the JSON data returned from the API
    print(data)
else:
    print('Error:', response.status_code)

# PUT request
payload = {'name': 'John Doe', 'email': 'johndoe@example.com'}
response = requests.put('https://api.example.com/users/1', json=payload)
if response.status_code == 200:
    data = response.json()
    # Process the JSON data returned from the API
    print(data)
else:
    print('Error:', response.status_code)

# DELETE request
response = requests.delete('https://api.example.com/users/1')
if response.status_code == 204:
    print('User deleted successfully')
else:
    print('Error:', response.status_code)