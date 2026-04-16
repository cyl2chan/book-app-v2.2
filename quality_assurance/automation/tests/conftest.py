"""
This module contain shared fixtures.
"""

import json
import pytest
import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_Options
from selenium.webdriver.chrome.service import Service as chrome_Service
from selenium.webdriver.firefox.options import Options as firefox_Options
from selenium.webdriver.firefox.service import Service as firefox_Service

# set up options for google chrome webdriver
chrome_options = chrome_Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Firefox
firefox_options = firefox_Options()


@pytest.fixture
def config(scope='session'):

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)
    print("config file opened")

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert config['implicit_wait'] > 0
    print("assert passed")
    
    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):

    # Initialise tbe WebDriver instance
    if config['browser'] == 'Firefox':
        firefox_service = firefox_Service("/snap/bin/geckodriver")
        b = webdriver.Firefox(service=firefox_service, options=firefox_options)
    elif config['browser'] == 'Headless Chrome':
        chrome_service = chrome_Service("/usr/bin/chromedriver")
        b = webdriver.Chrome(service=chrome_service, options=chrome_options)
    else: 
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b 

    # Quit the WebDriver instance for the cleanup
    b.quit()



