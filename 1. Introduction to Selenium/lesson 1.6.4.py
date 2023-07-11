# Task: Finding Elements with Selenium
# You need to open a page from a link and fill out a form on that page using Selenium. If everything is done correctly,
# then you will see a window with a verification code. This number you need to enter as an answer in this problem.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys('Eugene')
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("R")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Montreal")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Canada")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()

