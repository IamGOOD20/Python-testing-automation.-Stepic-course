# 1. Open page http://suninjuly.github.io/explicit_wait2.html
# 2. Wait for the price of the house to decrease to $100 (wait must be set to at least 12 seconds)
# 3. Click on the "Book" button
# 4. Solve a math problem we already know (use previously written code) and submit the solution

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import sin, log
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    book = browser.find_element(By.ID, 'book').click()

    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(log(abs(12*sin(x))))

    browser.find_element(By.ID, 'solve').click()

finally:
    sleep(5)
    browser.quit()
