import time
import csv
import undetected_chromedriver as uc
import pandas
import ssl
import certifi

ssl_context = ssl.create_default_context(cafile=certifi.where())

from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys

# Initialize Chrome driver
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")  # Helps evade bot detection
driver = uc.Chrome(options=options)
POST_URL = "https://www.facebook.com/UKCopHumour/posts/hi-is-there-a-chance-you-can-give-shout-out-to-pcs-bradley-and-pcs-griffin-from-/1879854272036855/"

COMMENTS_CSV = "facebook_comments.csv"
LIKES_CSV = "facebook_likes.csv"

options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")  # Helps evade detection
driver = uc.Chrome(options=options)

try:
    # Open Facebook

    driver.get("https://www.facebook.com/")
    time.sleep(3)

    # Navigate to the post
    driver.get(POST_URL)
    time.sleep(5)

    # Scroll to load more comments
    for _ in range(3):  # Adjust based on number of comments
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    # Extract comments
    comments_data = []
    comments = driver.find_elements(By.XPATH, "//div[@aria-label='Comment']")
    for comment in comments:
        try:
            author = comment.find_element(By.XPATH, ".//h3//span").text
            text = comment.find_element(By.XPATH, ".//div[@dir='auto']").text
            timestamp = comment.find_element(By.XPATH, ".//abbr").get_attribute("data-tooltip-content")
            comments_data.append([author, text, timestamp])
        except:
            pass

    # Save comments to CSV
    with open(COMMENTS_CSV, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Author", "Comment", "Timestamp"])
        writer.writerows(comments_data)

    print(f"✅ Saved {len(comments_data)} comments to {COMMENTS_CSV}")

    # Extract number of likes
    try:
        likes_element = driver.find_element(By.XPATH, "//span[contains(text(),'Like')]/following-sibling::span")
        likes_count = likes_element.text
        print(f"👍 Likes: {likes_count}")
    except:
        likes_count = "N/A"
        print("⚠ Could not retrieve likes count.")

    # Try to extract like usernames (if visible)
    likes_data = []
    try:
        driver.find_element(By.XPATH, "//span[contains(text(),'Like')]/parent::button").click()
        time.sleep(3)
        likers = driver.find_elements(By.XPATH, "//div[@role='dialog']//span[@dir='auto']")
        for liker in likers:
            likes_data.append([liker.text])
    except:
        print("⚠ Could not retrieve individual likers.")

    # Save likes to CSV
    with open(LIKES_CSV, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Liker Name"])
        writer.writerows(likes_data)

    print(f"✅ Saved {len(likes_data)} likes to {LIKES_CSV}")

finally:
    driver.quit()