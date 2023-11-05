import re
from playwright.sync_api import expect


class Page:
    def __init__(self, page) -> None:
        self.page = page

    def navigate(self, URL) -> None:
        self.page.goto(URL)

    def have_title(self, text) -> None:
        expect(self.page).to_have_title(re.compile(text))
