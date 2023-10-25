import concurrent.futures  # Importing concurrent.futures for concurrent execution
import multiprocessing  # Importing multiprocessing for parallel processing
import requests  # Importing the requests library for making HTTP requests


# Function to download a file given its URL and filename
def downloadFile(url, name):
    print(f"Start for {name}.jpg")  # Printing start message for download
    response = requests.get(url)  # Making a request to the given URL
    open(f"Photos/{name}.jpg", "wb").write(response.content)  # Writing the response content to a file
    print(f"{name}.jpg done")  # Printing completion message for download


# Function to download a set of predefined files
def normalFile():
    # Predefined URLs to download files
    Url = ["http://fvalk.com/images/Space/Asteroids/200001111800AV1_n.jpg",
           "http://fvalk.com/images/Space/Mercury/MERCURY!.JPG",
           "https://apod.nasa.gov/apod/image/2309/BlueHorse_Grelin_9342.jpg"]

    for link in Url:  # Looping through each URL
        print(link)  # Printing the URL
        filename = link.split('/')[-1]  # Extracting the filename from the URL
        downloadFile(link, filename[:-4])  # Calling the downloadFile function to download the file


# Function to download multiple files concurrently
def multiFile():
    global pros  # Using the global variable 'pros'
    for i in range(5):  # Looping 5 times
        p = multiprocessing.Process(target=downloadFile, args=[url, i])  # Creating a process for downloadFile
        p.start()  # Starting the process
        pros.append(p)  # Appending the process to the list of processes
    for p in pros:  # Looping through the processes
        p.join()  # Waiting for the process to complete


# Entry point of the script
if __name__ == '__main__':
    url = "https://picsum.photos/5000/5000"  # URL for file download
    pros = []  # List to hold process objects

    # Using a ProcessPoolExecutor for concurrent file downloads
    with concurrent.futures.ProcessPoolExecutor() as executor:
        URL = [url for i in range(101)]  # Creating a list of URLs to download
        L = [i for i in range(101)]  # Creating a list of indices
        result = executor.map(downloadFile, URL, L)  # Mapping the downloadFile function to the URLs and indices
        for r in result:  # Looping through the results
            print(r)  # Printing the result
