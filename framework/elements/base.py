from selenium.webdriver.common.by import By


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

    def find_element(self):
        return self.driver.find_element(self.locator_type, self.locator)
