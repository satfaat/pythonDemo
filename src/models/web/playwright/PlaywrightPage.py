

class PlaywrightPage:
    def __init__(self, page):
        self.page = page

        self.link_get_started = page.get_by_role("link", name="Get started")