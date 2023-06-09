from framework.pages import qase as qase_pages
from framework.pages.base import BasePage

from framework.elements.button import Button
from config.config import settings
from framework.elements.text_input import TextInput


class CreateNewProjectWindow:
    def __init__(self, driver):
        self.driver = driver

        self.project_name_inp = TextInput.css("#project-name")
        self.project_code_inp = TextInput.css("#project-code")
        self.project_description_inp = TextInput.css("#description-area")
        self.create_btn = Button.css("[type=submit]")

    def fill_and_confirm(self, name, code, description):
        self.project_name_inp.fill(name)
        self.project_code_inp.clear_and_fill(code)
        self.project_name_inp.fill(description)
        self.create_btn.click()

        return qase_pages.project.ProjectPage(self.driver)


class ProjectsPage(BasePage):
    _url = f"{settings.qase.ui.base_url}/projects"

    def __init__(self, driver):
        super().__init__(driver)

        self.create_btn = Button.css("#createButton")

    def open_create_new_window(self):
        self.create_btn.click()
        return CreateNewProjectWindow(self.driver)
