import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url)

    if response.status_code == 200:
        # Load the JSON response and pretty print it
        formatted_response = json.dumps(response.json(), indent=4)
        print("Formatted Response JSON:")
        print(formatted_response)
    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", str(e))
