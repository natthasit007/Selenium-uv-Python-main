import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1440, 1000)
    
    yield driver
    
    driver.quit()