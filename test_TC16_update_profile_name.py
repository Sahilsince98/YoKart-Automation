from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://demo.yo-kart.com/admin/admin-guest/login-form"
USERNAME = "admin"
PASSWORD = "admin@123"

def test_update_name_and_verify_in_dropdown():
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

    if "/admin/home" not in driver.current_url:
        print("❌ Login failed or dashboard not loaded.")
        driver.quit()
        return
    print("✅ Logged in and dashboard loaded.")

    # Step 2: Open Profile dropdown
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/header/div/div/div[2]/div/div[6]/a/span/img').click()
    time.sleep(2)

    # Step 3: Click "My Profile"
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/header/div/div/div[2]/div/div[6]/div/nav[1]/a[1]').click()
    time.sleep(3)

    # Step 4: Update the name field
    full_name_input = driver.find_element(By.NAME, "admin_name")
    new_name = "QA Test User"
    full_name_input.clear()
    full_name_input.send_keys(new_name)

    # Step 5: Click Update
    driver.find_element(By.XPATH, '//button[@type="submit" and contains(text(), "Update")]').click()
    time.sleep(3)

    print("✅ Name updated in profile form.")

    # Step 6: Refresh and re-open dropdown
    driver.get("https://demo.yo-kart.com/admin/home")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/header/div/div/div[2]/div/div[6]/a/span/img').click()
    time.sleep(2)

    # Step 7: Verify updated name appears
    displayed_name = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/header/div/div/div[2]/div/div[6]/div/div[1]/div/div[2]/h6').text.strip()

    if new_name in displayed_name:
        print(f"✅ Name successfully updated and shown in dropdown: {displayed_name}")
    else:
        print(f"❌ Name update failed. Dropdown shows: {displayed_name}")

    driver.quit()

test_update_name_and_verify_in_dropdown()
