import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.close()
