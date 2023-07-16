# 1. Open page http://suninjuly.github.io/file_input.html
# 2. Fill in text fields: first name, last name, email
# 3. Upload file. The file must have a .txt extension and may be empty
# 4. Press the "Submit" button
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


path = os.path.abspath(os.path.dirname(__file__))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    data = ['first_name', 'second_name', 'mail']
    [input.send_keys(value) for input, value in zip(browser.find_elements(By.CLASS_NAME, 'form-control'), data)]

    browser.find_element(By.ID, 'file').send_keys(path, '/test.txt')

    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:

    time.sleep(10)
    browser.quit()