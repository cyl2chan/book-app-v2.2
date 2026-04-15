"""
This module contain shared fixtures.
"""

import json
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
        b = selenium.webdriver.Firefox()
        print("firefox browser")
    elif config['browser'] == 'Headless Chrome':
        print("Headless Chrome browser")
        service = Service ("/usr/bin/chromedriver")
        b = webdriver.Chrome(service=service, options=options)
    else: 
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b 

    # Quit the WebDriver instance for the cleanup
    b.quit()



