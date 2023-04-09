import pytest

from config.config import settings
from framework.api.qase import QaseApi
from framework.helpers import fake_words
from framework.pages.qase.login import LoginPage
from framework.pages.qase.project import ProjectPage

from framework.fixtures.get_driver import driver


def test_open_by_url(driver):
    login_pg = LoginPage(driver).open_by_url()
    login_pg.login(settings.qase.login, settings.qase.password)

    project_pg = ProjectPage(driver).open_by_url(resource="RK")
    assert project_pg.project_code.text.startswith("RK")  # RK - any project code, hardcoded for example


def test_e2e(driver):
    login_pg = LoginPage(driver).open_by_url()
    projects_pg = login_pg.login(settings.qase.login, settings.qase.password)
    create_new_project_window = projects_pg.open_create_new_window()

    project_name = fake_words.random_text()
    project_code = "".join([word[0].upper() for word in project_name.split()])
    project_pg = create_new_project_window.fill_and_confirm(name=project_name, code=project_code, description="")

    assert project_pg.project_code.text.startswith(project_code)


def test_with_api_and_ui_e2e(driver):
    qase_api = QaseApi()

    project_name = fake_words.random_text()
    project_code = "".join([word[0].upper() for word in project_name.split()])

    response = qase_api.projects.create_new_project_v1(
        title=project_name,
        code=project_code
    )
    assert response["status"] is True
    api_project_code = response["result"]["code"]
    assert api_project_code == project_code

    login_pg = LoginPage(driver).open_by_url()
    login_pg.login(settings.qase.login, settings.qase.password)
    project_pg = ProjectPage(driver).open_by_url(resource=api_project_code)
    assert project_pg.project_code.text.startswith(api_project_code)


def test_with_api_e2e(driver):
    qase_api = QaseApi()

    project_name = fake_words.random_text()
    project_code = "".join([word[0].upper() for word in project_name.split()])

    create_project_resp = qase_api.projects.create_new_project_v1(
        title=project_name,
        code=project_code
    )
    assert create_project_resp["status"] is True
    api_project_code = create_project_resp["result"]["code"]
    assert api_project_code == project_code

    get_project_resp = qase_api.projects.get_project_by_code_v1(api_project_code)
    assert get_project_resp["result"]["code"] == api_project_code
    assert get_project_resp["result"]["title"] == project_name
