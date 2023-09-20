from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
print(type(driver))

driver.get("https://software.khuramtiles.com/Reports/account_ledger")
