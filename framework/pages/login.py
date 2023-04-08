from framework import pages
from framework.elements.text_input import TextInput


class LoginPage(pages.base.BasePage):
    _url = "https://app.qase.io/login"

    def __init__(self, driver):
        super().__init__(driver)

        self.email = TextInput.css("#inputEmail")
        self.password = TextInput.css("#inputPassword")

    def login(self, email, password):
        self.email.send_keys(email)
        self.password.send_keys(password)
