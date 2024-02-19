
import pytest
from playwright.sync_api import sync_playwright, Browser


# Define a fixture to create a browser instance
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


# Define a fixture to create a browser context for each test
@pytest.fixture(scope="function")
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()
