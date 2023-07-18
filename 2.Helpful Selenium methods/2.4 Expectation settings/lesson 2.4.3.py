# 1. Open page http://suninjuly.github.io/wait1.html
# 2. Click on the "Verify" button
# 3. Check that the message "Verification was successful!"


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
browser.implicitly_wait(5)

button = browser.find_element(By.ID, "verify")
button.click()


message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text