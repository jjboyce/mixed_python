from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set up Chrome options
options = Options()
#options.add_argument("--headless")  # Run in headless mode (no UI)
#options.add_argument("--disable-gpu")  # Recommended for headless mode
options.add_argument("--window-size=1920x1080")  # Set browser size

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open a webpage
    url = "https://www.sidolidesserts.co.uk/"
    driver.get(url)

    # Wait for elements to load (useful for dynamic sites)
    time.sleep(1)  # Adjust based on the site's speed

    # Extract page title
    title = driver.title
    print(f"Page Title: {title}")

    # Extract all links on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    element = driver.find_element("TextArea")
    
    for link in links:
        print(link.get_attribute("href"))
    
    ## searches for 'search term'

    

    time.sleep(10)

finally:
    # Quit the driver
    driver.quit()