# 1. open page
# 2. log in to the page with your username and password (see previous step)
# 3. enter the correct answer (the field before entering must be empty)
# 4. click the "Submit" button
# 5. wait for feedback that the answer is correct
# check that the text in the optional feedback is exactly the same as "Correct!"

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'https://stepik.org/lesson/236895/step/1'

@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test')
    browser = webdriver.Chrome()

    yield browser
    print('\nquit browser')
    browser.quit()

@pytest.mark.parametrize('links', ['https://stepik.org/lesson/236895/step/1',
                                   'https://stepik.org/lesson/236896/step/1',
                                   'https://stepik.org/lesson/236897/step/1',
                                   'https://stepik.org/lesson/236898/step/1',
                                   'https://stepik.org/lesson/236899/step/1',
                                   'https://stepik.org/lesson/236903/step/1',
                                   'https://stepik.org/lesson/236904/step/1',
                                   'https://stepik.org/lesson/236905/step/1'
                                   ])



class TestStepik:

    def test_autorisation_and_input_answer_stepik_page(self, browser, links):
        browser.implicitly_wait(30)
        browser.get(links)
        browser.find_element(By.CLASS_NAME, 'navbar__auth_login').click()
        browser.find_element(By.ID, 'id_login_email').send_keys('#')
        browser.find_element(By.ID, 'id_login_password').send_keys('#')
        browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
        sleep(6)

        browser.find_element(By.CLASS_NAME, 'ember-text-area').send_keys(math.log(int(time.time())))


        # browser.find_element(By.CLASS_NAME, 'submit-submission').click()  # submit-submission
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))).click()


        #result = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
        result = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//pre[@class="smart-hints__hint"]'))).text
        #result = browser.find_element(By.CLASS_NAME, 'attempt-message_wrong').text
        #print(result)
        sleep(20)
        assert "Correct!" == result

if __name__ == '__main__':
    pytest.main()




# find on GitHub:
# import pytest
# import time
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# message = ''
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")
# links = ['https://stepik.org/lesson/236895/step/1',
#          'https://stepik.org/lesson/236896/step/1',
#          'https://stepik.org/lesson/236897/step/1',
#          'https://stepik.org/lesson/236898/step/1',
#          'https://stepik.org/lesson/236899/step/1',
#          'https://stepik.org/lesson/236903/step/1',
#          'https://stepik.org/lesson/236904/step/1',
#          'https://stepik.org/lesson/236905/step/1', ]
#
#
# def answer():
#     return math.log(int(time.time()))
#
#
# @pytest.fixture
# def browser():
#     print("\nStarting Chrome browser.................")
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.implicitly_wait(10)
#     yield browser
#     print("\nTest finished........Quit browser........")
#     browser.quit()
#
#
# def collector(text):
#     with open('temp.txt', 'a') as file:
#         print(text, file=file)
#
#
#
# @pytest.mark.parametrize('link', links)
# def test_secret_message(browser, link):
#     browser.get(link)
#
#     input_textarea = browser.find_element(By.XPATH, '//textarea[@placeholder="Напишите ваш ответ здесь..."]')
#     input_textarea.send_keys(answer())
#
#     button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Отправить"]')))
#     button.click()
#     result = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//pre[@class="smart-hints__hint"]'))).text
#     if result != 'Correct!':
#         collector(result)
#     assert result == 'Correct!', f'expected \'Correct!\', got \'{result}\''
#
#
#
#
# if __name__ == '__main__':
#     pytest.main()