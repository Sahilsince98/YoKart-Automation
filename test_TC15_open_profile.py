from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://demo.yo-kart.com/admin/admin-guest/login-form"
USERNAME = "admin"
PASSWORD = "admin@123"

def test_login_and_open_profile():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    time.sleep(2)

    # Step 1: Login
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys(USERNAME)

    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)

    driver.find_element(By.NAME, "btn_submit").click()
    time.sleep(3)

    # Step 2: Verify Dashboard
    if "/admin/home" not in driver.current_url:
        print("❌ Login failed or dashboard not loaded.")
        driver.quit()
        return
    else:
        print("✅ Logged in and dashboard loaded.")

    try:
        # Step 3: Click profile icon in header (using full XPath)
        profile_icon = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/header/div/div/div[2]/div/div[6]/a/span/img')
        profile_icon.click()
        time.sleep(2)

        # Step 4: Click "My Profile" in the dropdown
        my_profile = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/header/div/div/div[2]/div/div[6]/div/nav[1]/a[1]')
        my_profile.click()
        time.sleep(3)

        # Step 5: Verify profile page
        if "/admin/profile" in driver.current_url:
            print("✅ My Profile page opened successfully.")
        else:
            print("❌ Failed to open My Profile page.")

    except Exception as e:
        print(f"❌ Error occurred: {e}")

    driver.quit()

# Run the test
test_login_and_open_profile()
