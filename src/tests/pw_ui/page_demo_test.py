import re
from playwright.sync_api import expect
from src.lbry.logs.log import LOGGER
from src.models.web.Page import Page
from src.models.web.playwright.PlaywrightPage import PlaywrightPage


URL_1 = 'https://playwright.dev/'
URL_2 = 'https://playwright.dev/docs/intro'
title_1 = 'Playwright'


def test_page_demo(context) -> None:
    page_1 = context.new_page()

    route = Page(page_1)
    route.navigate(URL_1)
    route.have_title(title_1)

    pw = PlaywrightPage(page_1)

    page_2 = context.new_page()
    route_2 = Page(page_2)
    route_2.navigate(URL_2)
