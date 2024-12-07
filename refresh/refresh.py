from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import pickle
import time
import os

# Load environment variables from the .env file
load_dotenv()

# Access the variables
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
DEPOP_PROFILE_URL = os.getenv("DEPOP_PROFILE_URL")

# Path to save/load cookies
COOKIES_FILE = 'depop_cookies.pkl'

def save_cookies(driver, cookies_path):
    """
    Save browser cookies to a file after manually logging in.
    """
    input("Log in to Depop in the browser, then press Enter...")
    with open(cookies_path, "wb") as cookie_file:
        pickle.dump(driver.get_cookies(), cookie_file)
    print(f"Cookies saved to {cookies_path}")


def load_cookies(driver, cookies_path):
    """
    Load cookies from a file and use them in the current browser session.
    """
    if not os.path.exists(cookies_path):
        raise FileNotFoundError(f"No cookie file found at {cookies_path}. Run save_cookies() first.")
    driver.get("https://www.depop.com")
    with open(cookies_path, "rb") as cookie_file:
        cookies = pickle.load(cookie_file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.refresh()
    print("Cookies loaded and session refreshed!")

def scroll_to_load_all_items(driver):
    """
    Navigates to page & Scrolls to the bottom of the page repeatedly to trigger lazy loading of items.
    """

    SCROLL_PAUSE_TIME = 2  # Adjust based on how long the page takes to load new items
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Exit the loop if no new content is loaded
        last_height = new_height

    print("Finished scrolling, all items should be loaded.")

def find_unsold_items(driver):

    # Close the tab and switch back
    driver.get(DEPOP_PROFILE_URL)
    time.sleep(2) 

    #scrolls to the bottom of page to load all items
    scroll_to_load_all_items(driver)

    items = driver.find_elements(By.XPATH, "//*[contains(@class, 'styles_productImageContainer')]")

    unsold_items = []
    for item in items:
        try:
            # Check if the item has a gradient overlay (sold items)
            gradient_overlay = item.find_element(By.XPATH, ".//div[contains(@class, 'styles_gradientOverlay')]")
            if gradient_overlay:
                continue
        except Exception:
            # No gradient overlay found, consider it unsold
            unsold_items.append(item)

    return unsold_items

def click_save_button(driver):
    try:
        save_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'SaveButton')]"))
        )
        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
        save_button.click()
        time.sleep(2)  # Wait for the action to complete
    except Exception as e:
        print(f"Error clicking the Save changes button: {e}")


def refresh_items(driver):
    """
    Refreshes Depop Items.
    """
    processed_items = set()  # To track already refreshed items
    items = find_unsold_items(driver)
    print(f"Found {len(items)} unsold items to refresh.")

    while True:

        items = find_unsold_items(driver) 

        # Get the first item in the list
        item = items[-1] # should be the last item?

        # Get the item's link
        item_link = item.find_element(By.XPATH, ".//a").get_attribute("href")

        # Skip if this item has already been processed
        if item_link in processed_items:
            print("First item encountered again. Breaking the loop.")
            break

        processed_items.add(item_link)  # Mark this item as processed
    
        # Navigate to the item's link
        driver.get(item_link)
        time.sleep(2)

         # Click edit and save, depending on Depop's UI
        try:
            edit_button = driver.find_element(By.XPATH, "//a[contains(@href, '/products/edit/')]")
            edit_button.click()
            time.sleep(2)

            click_save_button(driver)

        except Exception as e:
            print(f"Could not refresh item: {e}")
      

if __name__ == "__main__":
    # Set up ChromeDriver
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    try:
        # Uncomment the next line to save cookies (only needed once)
        # save_cookies(driver, COOKIES_FILE)

        # Load cookies and log in automatically
        load_cookies(driver, COOKIES_FILE)

        driver.get(DEPOP_PROFILE_URL)
        time.sleep(5)  # Wait for the page to load

        # Refresh all items on your Depop profile
        refresh_items(driver)

    finally:
        driver.quit()
