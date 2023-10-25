import argparse
import requests


def download_file(url, local_filename):
    """
    Downloads a file from the given URL and saves it with the specified local filename.

    Parameters:
    url (str): The URL of the file to download.
    local_filename (str): The desired local filename for saving the downloaded file.

    Returns:
    str: The local filename where the file is saved.
    """
    if local_filename is None:
        local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


# Create an argument parser
parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("-o", "--output", type=str, help="Name of the file to save", default=None)
args = parser.parse_args()

# Print the provided URL and output filename
print("URL:", args.url)
print("Output Filename:", args.output)

# Call the download_file function to download the file
downloaded_filename = download_file(args.url, args.output)

# Print the local filename where the file is saved
print("File downloaded and saved as:", downloaded_filename)

"""CMD python CH58_command_line_utility.py https://www.nasa.gov/sites/default/files/styles/full_width_feature/public
/thumbnails/image/iss065e473253.jpg spacePhoto.jpg python CH58_command_line_utility.py 
https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/thumbnails/image
/hubble_runawayblackhole_stsci-01gx657xta7kn3a8rpsdxs9d07.png -o blackhole.jpg"""
