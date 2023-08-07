import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', help='Choose browser language')# language=None


@pytest.fixture(scope='function')
def browser(request):
    print('\nfinal project start browser')
    browser = webdriver.Chrome()
    language = request.config.getoption('language')

    # language = None
    if language == 'ru':
        pass
    elif language == 'en':
        pass
    elif language =='es':
        pass
    else:
        raise pytest.UsageError('--language must be "ru" or "en" or "es"')



    yield browser
    print('\nfinal project quit browser')
    browser.quit()




