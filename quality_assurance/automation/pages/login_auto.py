"""
This module contains the page object for the login page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

class LoginPageAuto:

    # URL
    URL = "https://book-app-v2-2.onrender.com/login"

    # locators
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")

    # initialiser
    def __init__(self, browser):
        self.broswer = browser

    # interaction methods
    def load(self):
        self.browser.get(self.URL)

    def login_credentials(self, email, password):
        #email_input = self.browser.find_element(*self.EMAIL_INPUT)
        #password_input = self.browser.find_element(*self_PASSWORD_INPUT)
        login_input = self.browser.find_element(*self.EMAIL_INPUT, *self.PASSWORD_INPUT)
        login_input.send_keys(email + password + Keys.RETURN)