# 1.Open http://suninjuly.github.io/get_attribute.html page.
# 2.Find a picture element on it, which is an image of a treasure chest.
# 3.Take the value of the valuex attribute from this element, which is the x value for the task.
# 4.Calculate the mathematical function of x (the function itself remains unchanged).
# 5.Enter your answer in the text field.
# 6.Mark the checkbox "I'm the robot".
# 7.Select radiobutton "Robots rule!".
# 8.Click on the "Submit" button.


from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    find_chest = browser.find_element(By.ID, 'treasure')
    check_valuex = find_chest.get_attribute('valuex')

    insert_answer = calc(check_valuex)

    browser.find_element(By.ID, 'answer').send_keys(insert_answer)

    browser.find_element(By.ID, 'robotCheckbox').click()

    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(10)
    browser.quit()

