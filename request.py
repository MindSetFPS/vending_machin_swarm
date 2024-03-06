import requests
import json

url = 'http://127.0.0.1:7777/api'

def create_product(endpoint):
    # Define the URL you want to send the POST request to
    # Define the data you want to send in the POST request (if any)
    data = {
        'name': 'Sabritas',
        'price': '20',
        "code" : "A1",
    }

    headers = {
        'Content-Type': 'application/json',
    }

    # Send the POST request
    response = requests.post(url + endpoint, json=data, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response data
        print('Response:', response.json())
    else:
        # Print an error message if the request was unsuccessful
        print('Error:', json.dumps(response.json()))

def get_all_products(endpoint):
    response = requests.get(url + endpoint)

    if response.status_code == 200:
        # Print the response data
        print('Response:', response.json())
    else:
        # Print an error message if the request was unsuccessful
        print('Error:', json.dumps(response.json()))

get_all_products(endpoint="/products")

# create_product(endpoint="/products/create")