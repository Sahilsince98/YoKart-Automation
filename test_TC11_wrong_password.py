from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://demo.yo-kart.com/admin/admin-guest/login-form"
USERNAME = "admin"
WRONG_PASSWORD = "wrongpass"

def test_wrong_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    time.sleep(2)

    # Enter valid username
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys(USERNAME)

    # Enter invalid password
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(WRONG_PASSWORD)

    # Click login
    driver.find_element(By.NAME, "btn_submit").click()
    time.sleep(3)

    current_url = driver.current_url
    if "login-form" in current_url:
        print("✅ Wrong password test passed — Login was blocked.")
    else:
        print("❌ Wrong password test failed — Unexpected redirection.")

    driver.quit()

test_wrong_password()
