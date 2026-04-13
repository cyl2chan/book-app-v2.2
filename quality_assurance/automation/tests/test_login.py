"""
These tests cover the login of the Book App.
"""

from pages.login_auto import LoginPageAuto
from pages.library_auto import LibraryPageAuto

def test_login_credentials(browser):
    login_page = LoginPageAuto(browser)
    library_page = LibraryPageAuto(browser)
    EMAIL = "student@ryerson.ca"
    PASSWORD = "secret"

    # Given the login page is displayed
    login_page.load()
    
    # When the user enter "student_ryerson.ca" as email and "secret" as password
    login_page.login_credentials(EMAIL, PASSWORD)

    # Then the Library page is displayed
    library_page.load()

    # TODO REmove this exception once the test is complete
    raise Exception("Incomplete Test")

