from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the browser
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.co.uk")

    # Wait for the cookie popup and accept it
    try:
        cookie_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accept all')]"))
        )
        cookie_button.click()
        print("Cookies accepted!")
    except:
        print("No cookie popup found.")

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")

    # Enter search query
    search_query = "latest AI research"
    search_box.send_keys(search_query)

    # Press Enter
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
    )

    # Extract search result titles and links
    results = driver.find_elements(By.CSS_SELECTOR, "h3")

    print("\nTop search results:")
    for i, result in enumerate(results[:5], start=1):
        print(f"{i}. {result.text}")

finally:
    # Close the browser
    driver.quit()