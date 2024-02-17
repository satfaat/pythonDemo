
class SearchPageLoc:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page\
            .locator('[aria-label="Enter your search term"]')


class SearchPage(SearchPageLoc):
    def __init__(self, page):
        super().__init__(page)

    def navigate(self):
        self.page.goto("https://bing.com")

    def search(self, text):
        self.search_term_input.fill(text)
        self.search_term_input.press("Enter")
