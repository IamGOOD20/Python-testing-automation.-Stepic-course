# Your program must follow these steps:
#
# 1. Open the page https://suninjuly.github.io/math.html.
# 2. Read value for variable x.
# 3. Calculate the mathematical function of x (the code for this is given below).
# 4. Enter your answer in the text field.
# 5. Mark the checkbox "I'm the robot".
# 6. Select radiobutton "Robots rule!".
# 7. Click on the Submit button.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()

    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()

    browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()

finally:
    time.sleep(10)
    browser.quit()


# from selenium import webdriver
# from math import log, sin
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/math.html")
#
# x = browser.find_element_by_css_selector('[id = "input_value"]').text
# browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))
#
# for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
#     browser.find_element_by_css_selector(selector).click()