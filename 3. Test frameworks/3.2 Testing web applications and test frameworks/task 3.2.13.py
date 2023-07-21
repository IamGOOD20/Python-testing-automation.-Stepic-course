# 1. Take tests from step - https://stepik.org/lesson/138920/step/11?unit=196194
# 2. Create a new file
# 3. Create a class with tests in it, which should inherit from unittest.TestCase by analogy with the previous step
# 4. Rewrite unittest style test for page http://suninjuly.github.io/registration1.html
# 5. Rewrite in unittest style the second test for the page http://suninjuly.github.io/registration2.html
# 6. Decorate final checks in unittest style tests, for example using the assertEqual check method
# 7. Run resulting tests from file
# 8. Look at the launch report and find the last line
# 9. Submit this line as an answer to this assignment

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestPage(unittest.TestCase):

    browser = webdriver.Chrome()


    def fill_form(self, link):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]').send_keys('E')
        self.browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys('R')
        self.browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys('mail')
        self.browser.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]').send_keys('+1')
        self.browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]').send_keys('CA')
        self.browser.find_element(By.CLASS_NAME, 'btn').click()
        return self

    def finall_text(self):
        return self.browser.find_element(By.TAG_NAME, 'h1').text


    def test_1(self):

        self.fill_form('http://suninjuly.github.io/registration1.html')
        self.assertEqual('Congratulations! You have successfully registered!', self.finall_text(), "Don't find the info")


    def test_2(self):

        self.fill_form('http://suninjuly.github.io/registration2.html')
        self.assertEqual('Congratulations! You have successfully registered!', self.finall_text(), "Don't find the info")

if __name__ == '__main__':
    unittest.main()