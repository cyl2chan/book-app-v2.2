"""
This module contain shared fixtures.
"""

import pytest
import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# set up options for webdriver
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

@pytest.fixture
def browser():

    # Initialise the ChromeDriver instance
    service = Service ("/usr/bin/chromedriver")
    #b = selenium.webdriver.Chrome()
    b = webdriver.Chrome(service=service, options=options)

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield b 

    # Quit the WebDriver instance for the cleanup
    b.quit()



