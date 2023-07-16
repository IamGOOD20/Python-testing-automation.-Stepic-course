# 1. Open page http://suninjuly.github.io/redirect_accept.html
# 2. Click on the button
# 3. Switch to new tab
# 4. Pass the captcha for the robot and get the number-answer

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import *

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element(By.CLASS_NAME, 'trollface').click()

    browser.switch_to.window(browser.window_handles[1])

    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(log(abs(12*sin(x))))

    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    sleep(10)
    browser.quit()