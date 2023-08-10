from selenium.webdriver.common.by import By
from time import sleep

class TestPageElements():
    def test_basket_bottom_solution2(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        sleep(30)
        assert len(browser.find_elements(By.CLASS_NAME, 'add-to-basket')), '"add to cart" button was not found'
