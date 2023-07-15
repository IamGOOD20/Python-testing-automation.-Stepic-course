# 1. Open the page https://SunInJuly.github.io/execute_script.html.
# 2. Read value for variable x.
# 3. Calculate the mathematical function of x.
# 4. Scroll down the page.
# 5. Enter your answer in the text field.
# 6. Select checkbox "I'm the robot".
# 7. Toggle radiobutton "Robots rule!".
# 8. Click on the "Submit" button.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from math import *

try:
    browser = webdriver.Chrome()
    browser.get('https://SunInJuly.github.io/execute_script.html')

    x = int(browser.find_element(By.ID, 'input_value').text)
    print(log(abs(12*sin(x))))

    answer = browser.find_element(By.ID, 'answer')

    #browser.execute_script("return arguments[0].scrollIntoView(true);")

    browser.execute_script("window.scrollBy(0, 100);")

    answer.send_keys(log(abs(12*sin(x))))

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(40)
    browser.quit()