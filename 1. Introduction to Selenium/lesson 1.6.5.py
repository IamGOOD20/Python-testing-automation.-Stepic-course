# Task: search for an element by text in a link
# 1.Add import math to the very top of your code
# 2.Add a command to the code that will open the page: http://suninjuly.github.io/find_link_text
# 3.Add a command that will find a link with text. The text of the link to be found is encrypted with the formula:
# str(math.ceil(math.pow(math.pi, math.e)*10000))
# (you can insert this expression into your code, or you can execute it in the interpreter, copy the result from there and use it in your code)
#
# 4.Add a command to click on the found link: it will take you to the registration form
#
# 5.Fill out the form with the script in the same way as you did in the previous step of the lesson
#
# 6.After successful completion, you will receive a code - send it as an answer to this task

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

search = str(math.ceil(math.pow(math.pi, math.e)*10000))

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    open_link = browser.find_element(By.LINK_TEXT, search)
    open_link.click()

    input_1 = browser.find_element(By.TAG_NAME, 'input')
    input_1.send_keys('Name')

    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Second name')

    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys('City')

    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Country')

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(15)
    browser.quit()
