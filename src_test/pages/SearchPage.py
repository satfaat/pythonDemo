from playwright.sync_api import Page
from src_test.pages.BasePage import BasePage


class _SearchPageLoc:
    def __init__(self, page: Page):
        self.page = page
        self.__search_box = page.locator("#sb_form_q")
        self.__search_button = page.locator("#sb_form_go")


class SearchPage1(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = _SearchPageLoc(page)

    def search(self, text):
        self.locators.__search_box.fill(text)
        self.locators.__search_button.click()


class SearchPage2(BasePage, _SearchPageLoc):
    def __init__(self, page):
        BasePage.__init__(page)
        _SearchPageLoc.__init__(page)
        

    def search(self, text):
        self.__search_box.fill(text)
        self.__search_button.click()
