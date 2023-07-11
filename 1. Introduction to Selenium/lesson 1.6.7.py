# In this task, you need to fill out a form (http://suninjuly.github.io/huge_form.html).
# With the help of it, the marketing department of company N wanted to collect detailed information about the users of
# its product. As a reward for filling out the form, a discount code is available.
# But marketers obviously overdid it by adding 100 required fields to the form and limiting the time to fill it out.
# Now only robots can do this task.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "[type=text]")
    for element in elements:
        element.send_keys("Answer")


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()



