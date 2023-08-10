import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def pytest_addoption(parser):
    parser.addoption('--language', action='store', help='language of browser can be: [ru, en, fr, es ...]')

@pytest.fixture(scope='class')
def browser(request):
    print('\nsolution 1 start browser')
    browser = webdriver.Chrome()
    language = request.config.getoption('language')
    if language:
        browser.get(link)
        Select(browser.find_element(By.TAG_NAME, 'select')).select_by_value(language)
        browser.find_element(By.XPATH, '//button[@class="btn btn-default"]').click()
    else:
        raise pytest.UsageError('parameter not specified --language="language"')
    yield browser
    print('\nsolution 1 quit browser')
    browser.quit()




