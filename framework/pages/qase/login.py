from framework.pages import qase as qase_pages
from framework.pages.base import BasePage

from framework.elements.text_input import TextInput
from framework.elements.button import Button
from config.config import settings


class LoginPage(BasePage):
    _url = f"{settings.qase.ui.base_url}/login"

    def __init__(self, driver):
        super().__init__(driver)

        self.email_inp = TextInput.css("#inputEmail")
        self.password_inp = TextInput.css("#inputPassword")
        self.login_btn = Button.css("#btnLogin")

    def login(self, email, password):
        self.email_inp.fill(email)
        self.password_inp.fill(password)
        self.login_btn.click()
        return qase_pages.projects.ProjectsPage(self.driver)
