from framework.pages.login import LoginPage

from framework.fixtures.get_driver import driver


def test_open(driver):
    login_pg = LoginPage(driver)
    login_pg.open_by_url()

    login_pg.login("hello", "world")
