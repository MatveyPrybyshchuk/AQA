import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.boards_page import BoardsPage
from pages.tasks_page import TasksPage
from elements.locators import LoginPageLocators

# Тест на лоиг пейджу
@pytest.mark.play
def test_login_into_app(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.verify_page_opened()

# Тест на страницу "Главная"
@pytest.mark.play
def test_login_into_dashboard_page(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.verify_page_opened()
    login_page.login("charlie@example.com", "password123")

    dashboard_page = DashboardPage(page)
    dashboard_page.verify_page_opened()
    dashboard_page.verify_empty_state()

# Тест на страницу "Все доски"
@pytest.mark.play
def test_login_into_boards_page(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.verify_page_opened()
    login_page.login("charlie@example.com", "password123")

    boards_page = BoardsPage(page)
    boards_page.open()
    boards_page.verify_page_opened()
    boards_page.verify_empty_state()


# Тест на страницу "Все задачи"
@pytest.mark.play
def test_login_into_tasks_page(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.verify_page_opened()
    login_page.login("charlie@example.com", "password123")

    tasks_page = TasksPage(page)
    tasks_page.open()
    tasks_page.verify_page_opened()
    tasks_page.verify_empty_state()

# Тест элемента юзера
@pytest.mark.play
def test_user_profile(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.verify_page_opened()
    login_page.login("charlie@example.com", "password123")

    user_profile = page.locator('.header-user-info')
    username = page.locator('.header-username')

    expect(user_profile).to_be_visible()
    expect(username).to_contain_text("charlie")

    user_profile.click()

    expect(page.locator(LoginPageLocators.USERNAME)).to_be_visible()
    expect(page.locator(LoginPageLocators.USER_EMAIL)).to_be_visible()
    expect(page.locator(LoginPageLocators.USER_AVATAR)).to_be_visible()
    expect(page.locator(LoginPageLocators.USER_LOGOUT_BTN)).to_be_visible()


# Логаут
@pytest.mark.play
def test_logout(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.verify_page_opened()
    login_page.login("charlie@example.com", "password123")

    boards_page = BoardsPage(page)
    boards_page.open()

    user_profile = page.locator('.header-user-info')

    user_profile.click()
    page.locator(LoginPageLocators.USER_LOGOUT_BTN).click()

    login_page.verify_page_opened()
