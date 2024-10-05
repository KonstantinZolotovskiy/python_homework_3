import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_config():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://www.google.com/ncr"

    yield

    browser.quit()
