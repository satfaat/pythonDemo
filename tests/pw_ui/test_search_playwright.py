from playwright.sync_api import BrowserContext
from src_test.pages.SearchPage import SearchPage2


def test_search_playwright(context: BrowserContext):
    # Define a test case that searches for "playwright" on Bing
    # Create a page object
    page = context.new_page()
    # Create a search page object
    search_page = SearchPage2(page)
    # Go to Bing.com
    search_page.go_to("https://www.bing.com")
    # Search for "playwright"
    search_page.search("playwright")
    # Wait for the results page to load
    page.wait_for_load_state("networkidle")
    # Assert that the first result contains "playwright.dev"
    assert "playwright.dev" in page\
        .locator("#b_results .b_algo:nth-child(1) cite")\
        .inner_text()
