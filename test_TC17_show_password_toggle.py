from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://demo.yo-kart.com/admin/admin-guest/login-form"

def test_show_password_functionality():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    time.sleep(2)

    # Step 1: Locate the password field and check its type before clicking show
    password_field = driver.find_element(By.NAME, "password")
    input_type_before = password_field.get_attribute("type")
    
    if input_type_before != "password":
        print(f"❌ Initial input type is not 'password'. Got: {input_type_before}")
        driver.quit()
        return
    else:
        print("✅ Password field type before toggle is 'password'.")

    # Step 2: Click the Show Password icon
    show_password_icon = driver.find_element(By.ID, "showPass")
    show_password_icon.click()
    time.sleep(1)

    # Step 3: Check if the input type changed to 'text'
    input_type_after = password_field.get_attribute("type")
    if input_type_after == "text":
        print("✅ Password field type after toggle is 'text'. Show password works.")
    else:
        print(f"❌ Password field type after toggle is still '{input_type_after}'. Show password failed.")

    driver.quit()

test_show_password_functionality()
