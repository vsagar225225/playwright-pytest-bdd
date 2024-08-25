# pages/home_page.py
from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://example.com")

    def get_title(self):
        return self.page.title()
