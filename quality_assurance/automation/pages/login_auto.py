"""
This module contains the page object for the login page.
"""

from selenium.webdriver.common.by import By

class LoginPageAuto:

    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")

    def __init__(self, browser):
        self.broswer = browser

    def load(self):
        #TODO
        pass

    def login_credentials(self, email, password):
        #TODO
        passed