from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the web driver
driver = webdriver.Firefox()

# Navigate to the login page
driver.get("https://software.khuramtiles.com/Main_action")

# Find and fill in the username and password fields
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("khuram")
password_field.send_keys("bismillah123")

# Submit the login form
login_form = driver.find_element(By.ID, "myform")
login_form.submit()

# Wait for the dropdown menu to appear
dropdown_menu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "li.dropdown.open ul.dropdown-menu")
    )
)

# Find the 6th li element within the dropdown menu (adjust the index as needed)
ledger_link = dropdown_menu.find_element(By.XPATH, "./li[6]/a")

# Click the link to navigate to the account ledger page
ledger_link.click()


# Close the browser when done
time.sleep(50)
driver.quit()
