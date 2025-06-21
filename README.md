YoKart Admin Panel - Manual Test Cases & Automation Script Guide

Project Overview

This test suite covers basic UI and functional automation of the YoKart Admin Login Panel available at:
🔗 https://demo.yo-kart.com/admin/admin-guest/login-form

All test scripts have been written in Python with Selenium, designed with simplicity and no dependencies on external modules like pages/, utils/, or Page Object Model structure. These are independent test scripts, suitable for beginners or demonstration purposes.

📂 Folder Structure

YoKartAutomation/
├── chromedriver.exe         # Chrome driver binary
├── config.py                # Global credentials or settings
├── test_TC01_logo_refresh.py
├── test_TC02_valid_login.py
├── test_TC03_invalid_login.py
├── test_TC04_open_profile.py
├── test_TC05_update_name.py
├── test_TC06_show_password.py
├── test_TC07_ui_cross_browser.py
├── test_TC08_restore_popup_content.py
├── test_TC09_restore_popup_contact_link.py
└── README.md                # Project documentation (this file)

💡 All scripts are standalone and independent — no reusable methods or page objects have been used.

Manual Test Cases

TC01 - Logo Refresh
Objective: Ensure clicking on the logo refreshes the page.
Steps:
Open login page.
Click the YoKart logo.
Expected: Page reloads successfully, same login form is visible.
Type: UI

TC02 - Valid Login
Objective: Verify login with correct credentials.
Steps:
Enter admin and admin@123
Click Login.
Expected: User is redirected to /admin/home.
Type: Functional

TC03 - Invalid Login
Objective: Handle incorrect password.
Steps:
Enter valid username, wrong password
Click Login.
Expected: User remains on login with error message.
Type: Negative

TC04 - Open Profile from Dropdown
Objective: Navigate to profile via top nav dropdown.
Steps:
Login → Click profile icon → Select "My Profile"
Expected: /admin/profile page opens.
Type: Navigation

TC05 - Update Profile Name
Objective: Ensure updated name reflects in dropdown.
Steps:
Change name in profile page → Click Update
Check name under profile icon
Expected: Name is updated successfully.
Type: Functional

TC06 - Show Password Toggle
Objective: Check show/hide password functionality.
Steps:
Click show password icon
Expected: Input type changes to text
Type: UI

TC07 - Cross Browser UI Test
Objective: Validate consistent layout in Chrome, Firefox, Edge
Steps:
Open login page in 3 browsers
Expected: Page renders properly in all
Type: Compatibility

TC08 - Restore Popup Content Verification
Objective: Check that popup contains accurate help content
Steps:
Click the gear icon → Popup appears
Expected: Contains support text, phone numbers, email, CTA
Type: Content Verification

TC09 - Restore Popup → Contact Page Redirection
Objective: Ensure contact button opens contact page
Steps:
Open restore popup → Click "Click here"
Expected: Redirects to https://www.yo-kart.com/contact-us.html
Type: External link test

⚙️ Setup Instructions

Clone/download this repo or create the structure manually.
Install requirements:
pip install selenium

Download ChromeDriver matching your browser version.
Place chromedriver.exe in root of the folder.

Run any script:
python test_TC02_valid_login.py

🔐 Login Credentials Used

Username: admin
Password: admin@123

✍️ Author Note

These test scripts were created with the help of ChatGPT (Selenium QA Expert prompt) to demonstrate basic test case design, UI validation, and functional testing. 

No Page Object Model (POM) or PyTest structure has been used here to maintain simplicity and readability.

