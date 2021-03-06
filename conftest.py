import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action = "store", default = "en",
                    help = "Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'intl.accept_languages':language})
    browser = webdriver.Chrome(options = options)
    print("\n Starting Chrome Browser for test..")
    yield browser
    print("\n Quit Browser...")
    browser.quit()
