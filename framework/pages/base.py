from selenium.webdriver.remote.webdriver import WebDriver
from urllib.parse import urlparse, urlencode, urljoin
from framework.elements.base import BaseElement


class BasePage:
    _url = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        BaseElement.set_driver(driver)

    def open_by_url(self, resource: str = None, params: dict = None):
        open_url = self._url
        if resource:
            open_url = urljoin(open_url, resource)

        if params is not None:
            url_parts = urlparse(self._url)
            url_parts = url_parts._replace(query=urlencode(params))
            open_url = url_parts.geturl()

        self.driver.get(open_url)
        return self
