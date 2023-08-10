import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="select language ")

@pytest.fixture(scope='function')
def browser(request):
    print('\nStart browser solution 2')
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if user_language:
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be selected")

    yield browser
    print('\nQuit browser solution 2')
    browser.quit()
