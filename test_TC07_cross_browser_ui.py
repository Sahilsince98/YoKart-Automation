from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


URL = "https://demo.yo-kart.com/admin/admin-guest/login-form"

def launch_browser_and_validate_ui(browser_name):
    driver = None
    try:
        if browser_name == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser_name == "edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            print(f"❌ Unsupported browser: {browser_name}")
            return

        driver.maximize_window()
        driver.get(URL)
        time.sleep(3)

        # Basic UI Checks
        assert "Yo!Kart" in driver.title, f"{browser_name}: Page title is incorrect."
        assert driver.find_element(By.NAME, "username").is_displayed(), "Username field not visible"
        assert driver.find_element(By.NAME, "password").is_displayed(), "Password field not visible"
        assert driver.find_element(By.NAME, "btn_submit").is_displayed(), "Login button not visible"

        # Screenshot
        driver.save_screenshot(f"{browser_name}_ui_check.png")
        print(f"✅ {browser_name.capitalize()} UI Test Passed and screenshot saved.")
        
    except Exception as e:
        print(f"❌ {browser_name.capitalize()} Test Failed: {e}")
    finally:
        if driver:
            driver.quit()


def test_cross_browser_ui():
    for browser in ["chrome", "firefox", "edge"]:
        launch_browser_and_validate_ui(browser)


# Run directly
if __name__ == "__main__":
    test_cross_browser_ui()
