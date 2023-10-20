from Browser import Browser
from Browser.utils.data_types import SupportedBrowsers

b = Browser(timeout="20 s", retry_assertions_for="500 ms")
b.new_browser(browser=SupportedBrowsers.firefox)
b.new_context(
    acceptDownloads=True,
    viewport={"width": 1920, "height": 1080},
    httpCredentials={"username": "admin", "password": "123456"},
)
b.new_page("https://playwright.dev")
assert b.get_text("h1") == "🎭 Playwright"
b.close_browser()