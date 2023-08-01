# 1. open the lesson in Chrome using the link https://stepik.org/lesson/236895/step/1
# 2. log in with your username and password
# 3. wait until the authorization pop-up is no more

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = 'https://stepik.org/lesson/236895/step/1'


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser')
    browser.quit()


class TestStepik:

    def test_autorisation_stepik_page(self, browser):
        browser.implicitly_wait(10)
        browser.get(link)
        browser.find_element(By.CLASS_NAME, 'navbar__auth_login').click()
        browser.find_element(By.ID, 'id_login_email').send_keys('rukshenas1990@gmail.com')
        browser.find_element(By.ID, 'id_login_password').send_keys('amgood')
        browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
        sleep(3)

