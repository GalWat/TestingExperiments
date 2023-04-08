from framework import pages
from framework.elements.label import Label
from config.config import settings


class ProjectPage(pages.base.BasePage):
    _url = f"{settings.qase.ui.base_url}/project"

    def __init__(self, driver):
        super().__init__(driver)

        self.project_code = Label.xpath('//*[@id="application-content"]/div/div[1]/h1')
