import requests
from bs4 import BeautifulSoup
import csv

# Get URL from user
url = input("Input URL to scrape: ")

# Set user agent to avoid blocking
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an error for bad status codes (e.g., 404, 500)
    
    print("Page Fetched Successfully!")

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract page title
    title = soup.title.text.strip() if soup.title else "No title found"
    print("\nPage Title:", title)

    # Extract headings
    headings = [h.text.strip() for h in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])]
    print("\nHeadings:", headings)

    # Extract all paragraph texts
    paragraphs = [p.text.strip() for p in soup.find_all("p")]
    print("\nParagraphs:", paragraphs[:3])  # Print only first 3 for preview

    # Extract all links
    links = [a["href"] for a in soup.find_all("a", href=True)]
    print("\nLinks:", links[:5])  # Print first 5 for preview

    # Extract meta descriptions
    meta_desc = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc["content"].strip() if meta_desc else "No meta description found"
    print("\nMeta Description:", meta_desc)

    # Save to CSV
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Meta Description", "Headings", "Paragraphs", "Links"])
        writer.writerow([title, meta_desc, headings, paragraphs, links])

    print("\nData saved to 'scraped_data.csv'!")

except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {e}")