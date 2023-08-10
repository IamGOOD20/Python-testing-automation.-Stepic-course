import pytest
from selenium.webdriver.common.by import By
from time import sleep

class TestPythonAnyware():
    def test_basket_bottom(self, browser):
        sleep(20)
        assert len(browser.find_elements(By.CLASS_NAME, 'add-to-basket')) == 1, '"add to cart" button was not found'

if __name__=='__main':
    pytest.main()