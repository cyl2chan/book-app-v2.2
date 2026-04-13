"""
This module contains the page object for the library page.
"""

class LibraryPageAuto:

    def __init__(self, browser):
        self.browser = browser

    def get_library(self):
        return "Library Page successfully loaded"
