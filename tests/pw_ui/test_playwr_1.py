import re
from playwright.sync_api import expect
from src.lbry.logs.log import LOGGER


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(context) -> None:

    page_1 = context.new_page()
    page_2 = context.new_page()

    page_1.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page_1).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page_1.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    page_2.goto('https://playwright.dev/docs/intro')
    page_2.get_by_label(
        "Switch between dark and light mode (currently dark mode)").click()

    if 0:
        with context.expect_page() as page_4:
            page_4.get_by_label(
                "GitHub repository").click()  # Opens a new tab
        new_page = page_4.value
        new_page.get_by_label("GitHub repository").click()
        LOGGER.info(f'new page is {new_page}')
        new_page.wait_for_load_state()
        print(new_page.title())

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page_1).to_have_url(re.compile(".*intro"))
