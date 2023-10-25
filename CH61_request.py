import requests

# URL of the API endpoint we want to access
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Sending a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Print the JSON response
        print("Response JSON:")
        print(response.json())
    else:
        # Print an error message if the request was unsuccessful
        print("Error:", response.status_code)

except requests.exceptions.RequestException as e:
    # Print an error message if an exception occurs during the request
    print("Error:", str(e))
