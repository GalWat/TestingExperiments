from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    driver = None

    @classmethod
    def set_driver(cls, driver):
        cls.driver = driver

    @classmethod
    def css(cls, locator):
        obj = cls(locator_type=By.CSS_SELECTOR, locator=locator)
        return obj

    @classmethod
    def xpath(cls, locator):
        obj = cls(locator_type=By.XPATH, locator=locator)
        return obj

    def __init__(self, locator_type, locator):
        self.locator_type = locator_type
        self.locator = locator

    def wait_to_be_visible(self, timeout=10, poll_frequency=1):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
        element = wait.until(EC.visibility_of_element_located((self.locator_type, self.locator)))
        return element

    def find_element(self, timeout=10, poll_frequency=1):
        element = self.wait_to_be_visible(timeout=timeout, poll_frequency=poll_frequency)
        return element
