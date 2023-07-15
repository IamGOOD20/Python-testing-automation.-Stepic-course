# 1. Open page https://suninjuly.github.io/selects1.html
# 2. Calculate the sum of given numbers
# 3. Select the value equal to the calculated amount in the drop-down list
# 4. Press the "Submit" button

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects1.html')

    calculate = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(calculate))

    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(10)
    browser.quit()