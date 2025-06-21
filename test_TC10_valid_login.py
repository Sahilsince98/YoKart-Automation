from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://demo.yo-kart.com/admin/admin-guest/login-form"
USERNAME = "admin"
PASSWORD = "admin@123"

def test_valid_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    time.sleep(2)

    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys(USERNAME)

    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)

    driver.find_element(By.NAME, "btn_submit").click()
    time.sleep(3)

    if "dashboard" in driver.current_url:
        print("✅ Login successful — redirected to dashboard.")
    else:
        print("❌ Login failed — still on login page.")

    driver.quit()

test_valid_login()
