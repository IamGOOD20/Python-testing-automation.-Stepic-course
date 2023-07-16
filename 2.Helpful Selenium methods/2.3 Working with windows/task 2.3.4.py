# 1. Open page http://suninjuly.github.io/alert_accept.html
# 2. Click on the button
# 3. Accept confirm
# 4. On the new page, solve the captcha for robots to get the number with the answer

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *



try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    browser.find_element(By.TAG_NAME, 'button').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    browser.get('http://suninjuly.github.io/alert_redirect.html?') # ?
    x = int(browser.find_element(By.ID, 'input_value').text)
    print(x)
    browser.find_element(By.ID, 'answer').send_keys(log(abs(12*sin(x))))

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()