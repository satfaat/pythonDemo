from playwright.sync_api import Page


class SearchPageLoc:
    def get_page(page: Page):
        return page
    search_term_input = page\
            .locator('[aria-label="Enter your search term"]')

    # def __init__(self, page: Page) -> None:
    #     self.page = page
    #     self.search_term_input = page\
    #         .locator('[aria-label="Enter your search term"]')


class SearchPage:
    # def __init__(self, page):
    #     super().__init__(page)

    def get_page(page: Page):
        return page

    def navigate(self):
        self.page.goto("https://bing.com")

    def search(text):
        SearchPageLoc.search_term_input.fill(text)
        SearchPageLoc.search_term_input.press("Enter")
