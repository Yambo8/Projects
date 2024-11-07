#This project is a Python-based tool designed to scan a specified website, extract all links from its HTML content, and selectively download files based on file type.
#Using the Requests library for HTTP interactions and BeautifulSoup for HTML parsing, the tool sends a request to the target URL, retrieves the HTML content, and identifies all links on the page.
#It then checks each link for specific file types (e.g., .pdf, .jpg, .png, .zip, .txt) and, if found, downloads the file to the user’s Desktop.
#The tool includes error handling to manage unsuccessful requests and only downloads files with valid HTTP responses, ensuring efficiency and reliability in gathering resources from the target site.

# Importing the Requests library for sending and receiving HTTP requests.
import requests
# Importing BeautifulSoup from bs4 to parse and process HTML content.
from bs4 import BeautifulSoup
# Importing the OS library for interacting with the operating system.
import os

# This function takes a URL and a local filename as parameters.
# It sends a GET request to the URL and saves the response content to local_filename.
def download_file(URL, local_filename):
    response = requests.get(URL)
    if response.status_code == 200:
        # Open the specified file to store the GET request's content in binary mode.
        with open(local_filename, 'wb') as file:
            file.write(response.content)
            print(f"Successfully downloaded {local_filename}")
    else:
        print(f"Failed to download {URL}")

# This function sends a GET request to the URL and uses BeautifulSoup to parse the HTML content.
def scan_website(URL):
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"Failed to access {URL}")
        return
    # Create a parse tree for extracting data from HTML.
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all 'a' tags with links, extracting valid paths.
    links = [link.get('href') for link in soup.find_all('a', href=True)]
    print("\nLinks on the website:")
    for link in links:
        # Skip NoneType entries (links without href attributes).
        if link is None:
            continue
        # Construct absolute URLs from relative paths.
        if link.startswith('/'):
            if link.startswith('//'):
                file_url = 'https:' + link
            else:
                file_url = URL + link
        else:
            file_url = link

        # Display the absolute URL associated with each link.
        print(f"{link} => {file_url}")

        # Identify and download specific file types.
        if any(file_url.lower().endswith(ext) for ext in ['.pdf', '.jpg', '.png', '.jpeg', '.zip', '.txt']):
            # Specify the file location on the Desktop.
            # os.path.basename extracts the filename from the URL's last segment.
            # os.path.join handles paths across different operating systems.
            file_name = os.path.basename(file_url)
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', file_name)
            # HEAD request retrieves file metadata without downloading it.
            head_response = requests.head(file_url)
            # If the resource is available (status code 200), download the file.
            if head_response.status_code == 200:
                print(f"\033[91mDownloading:\033[0m {file_url}")
                download_file(file_url, desktop_path)
            else:
                print(f"Failed to access file: {file_url}")

# Define the target website URL for scanning.
URL = 'https://www.' + input("Which domain would you like to scan?\n(e.g. google.com): ")
# Call scan_website function to begin the scan.
scan_website(URL)
