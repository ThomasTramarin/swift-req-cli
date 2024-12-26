import requests
import json
from requests.exceptions import ConnectionError, Timeout, RequestException

def make_request(method, url, data=None, headers=None):
    try:
        if data:
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                print("Invalid JSON data provided.")

        if headers is None:
            headers = {}

        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        elif method == "PATCH":
            response = requests.patch(url, json=data, headers=headers)
        
        response.raise_for_status()  # Exceptions for HTTP errors (4xx, 5xx)
        return response
    
    except ConnectionError:
        print("Connection error: Unable to reach the server.")
    except Timeout:
        print("The connection to the server has timed out.")
    except RequestException as e:
        print(f"Request error: {e}")
    return None