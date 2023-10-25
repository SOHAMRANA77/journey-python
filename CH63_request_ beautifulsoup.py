import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/blogpost/email-validator-using-html-css-js/"  # Replace with the desired URL

try:
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, "html.parser")

        # Print the formatted HTML content
        print("Formatted HTML Content:")
        print(soup.prettify())
        for heading in soup.findAll("h2"):
            print(heading)
    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", str(e))
