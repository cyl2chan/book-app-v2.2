"""
This module contains the page object for the library page.
"""

class LibraryPageAuto:

    # URL
    URL = "https://book-app-v2-2.onrender.com/library"

    def __init__(self, browser):
        self.browser = browser

    # interaction methods
    def load(self):
        self.browser.get(self.URL)

    def get_library(self):
        return "Library Page successfully loaded"
