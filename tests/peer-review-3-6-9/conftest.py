import pytest
from selenium import webdriver
from time import sleep


def pytest_addoption(parser):
    available_langs = (
        'ca', 'cs', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it', 'ko',
        'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'zh-hans', 'uk'
    )  # List (actually a tuple) of available languages for input validation.

    parser.addoption(
        '--language',
        action='store',
        default='en-gb',
        help='Set user language for the tests.',
        choices=available_langs
    )


@pytest.fixture
def browser(request):

    # Get the language option.
    user_language = request.config.getoption('--language')
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Initiate the browser using the option above.
    browser = webdriver.Chrome(options=opts)

    # Add implicit wait so the test doesn't fail if it takes a while to load the page.
    browser.implicitly_wait(10)

    yield browser

    # Wait a bit so that the reviewer can check if the language is correct.
    sleep(2)

    # Clean-up. Exit the browser.
    browser.quit()
