import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

class TestPythonAnyware():
#     def test_open_page(self, browser):
#         browser.get(link)

    def test_basket_bottom(self, browser):
        browser.get(link)
        sleep(30)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="Add to basket"]')))


if __name__=='__main':
    pytest.main()