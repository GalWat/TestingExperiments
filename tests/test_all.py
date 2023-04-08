from config.config import settings
from framework.pages.login import LoginPage

from framework.fixtures.get_driver import driver
from framework.helpers import fake_words


def test_e2e(driver):
    login_pg = LoginPage(driver).open_by_url()

    projects_pg = login_pg.login(settings.qase.login, settings.qase.password)

    create_new_project_window = projects_pg.open_create_new_window()

    project_name = fake_words.random_text()
    project_code = "".join([word[0].upper() for word in project_name.split()])

    project_pg = create_new_project_window.fill_and_confirm(name=project_name, code=project_code, description="")
    assert project_pg.project_code.text.startswith(project_code)
