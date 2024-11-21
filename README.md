## "Stori QA Automation Engineer Challenge"
Welcome to my Stori Challenge! 

![credit-cards](https://github.com/user-attachments/assets/693192f7-c1bc-42c9-98ca-35d360426c7f)

### Overview
This script automates various web-based tests using Selenium WebDriver with Python (Chrome Browser). It interacts with a sample web page from the URL https://rahulshettyacademy.com/AutomationPractice/. The script includes various test cases based on the documentation received.
### What do I need before running the code? (Requirements)
Before running this script, ensure you have the following installed:

**Python** (last version)
**Selenium - WebDriver** for browser automation. You can install it using pip

    pip install selenium
**Webdriver Manager** - Automatically handles the installation of the appropriate browser driver. Install it using pip:

    pip install webdriver-manager
In my case I used Chrome for automation.

### Dependencies
**datetime:** To log timestamps for test case execution.
**time:** To introduce delays (e.g., time.sleep()).
**selenium:** For interacting with web elements using Selenium WebDriver.
**webdriver_manager:** For managing ChromeDriver.

### **Known Issues**
- TestCase 7.1 (Web Table Counter): The counting logic is not working as expected. This part requires debugging to correctly count the rows with price $25.
- TestCase 4 and TestCase 5 (Switch Window and Switch Tab): Is not working as expected.

### Run the Script
To run the script, simply execute it in your terminal:

    python <stori_test>.py --browser=Chrome
