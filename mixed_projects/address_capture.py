##  address capture py

import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage to scrape
url = "https://geographic.org/streetview/england/north_west_england/greater_manchester/stockport/bramhall.html"  # Replace with the URL you want to scrape

# Send a request to fetch the content of the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <li> tags on the page
    items = soup.find_all('li')

    # Extract the text from each <li> and save it to a list
    item_texts = [item.get_text(strip=True) for item in items]

    # Define the output CSV file
    output_file = "bramhall_addresses.csv"

    # Write the extracted items to a CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header (optional)
        writer.writerow(['Item'])  # Add more headers if necessary
        
        # Write the list of items
        for item in item_texts:
            writer.writerow([item])

    print(f"Scraped {len(item_texts)} items and saved them to '{output_file}'")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")