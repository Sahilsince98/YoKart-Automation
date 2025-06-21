from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://demo.yo-kart.com/admin/admin-guest/login-form"

def test_logo_click_refreshes_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    time.sleep(2)

    # Capture the current page source
    before = driver.page_source

    # Click the logo
    logo = driver.find_element(By.CLASS_NAME, "logo")
    logo.click()
    time.sleep(2)

    after = driver.page_source

    if before != after:
        print("✅ Logo click refreshed the page.")
    else:
        print("❌ Logo click did not refresh the page.")

    driver.quit()

# Run the test
test_logo_click_refreshes_page()
