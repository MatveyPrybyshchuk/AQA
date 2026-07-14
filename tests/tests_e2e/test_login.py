import pytest
import allure
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.boards_page import BoardsPage
from pages.tasks_page import TasksPage

@allure.feature("TestBasePage")
class TestBasePage:
    @allure.title("test_login_into_app")
    @allure.description("test_login_into_app")
    @allure.tag("smoke")
    @pytest.mark.play
    def test_login_into_app(self, page: Page):
        login_page = LoginPage(page)
        login_page.open()

        login_page.verify_page_opened()

    @allure.title("test_login_into_dashboard_page")
    @allure.description("test_login_into_dashboard_page")
    @allure.tag("smoke")
    @pytest.mark.play
    def test_login_into_dashboard_page(self, page: Page):
        login_page = LoginPage(page)
        login_page.open()

        login_page.verify_page_opened()
        login_page.login("charlie@example.com", "password123")

        dashboard_page = DashboardPage(page)
        dashboard_page.verify_page_opened()
        dashboard_page.verify_empty_state()

    @allure.title("test_login_into_boards_page")
    @allure.description("test_login_into_boards_page")
    @allure.tag("smoke")
    @pytest.mark.play
    def test_login_into_boards_page(self, page: Page):
        login_page = LoginPage(page)
        login_page.open()

        login_page.verify_page_opened()
        login_page.login("charlie@example.com", "password123")

        boards_page = BoardsPage(page)
        boards_page.open()
        boards_page.verify_page_opened()
        boards_page.verify_empty_state()


    @allure.title("test_login_into_tasks_page")
    @allure.description("test_login_into_tasks_page")
    @allure.tag("smoke")
    @pytest.mark.play
    def test_login_into_tasks_page(self, page: Page):
        login_page = LoginPage(page)
        login_page.open()

        login_page.verify_page_opened()
        login_page.login("charlie@example.com", "password123")

        tasks_page = TasksPage(page)
        tasks_page.open()
        tasks_page.verify_page_opened()
        tasks_page.verify_empty_state()

    @allure.title("test_user_profile")
    @allure.description("test_user_profile")
    @allure.tag("smoke")
    @pytest.mark.play
    def test_user_profile(self, page: Page):
        login_page = LoginPage(page)
        login_page.open()

        login_page.verify_page_opened()
        login_page.login("charlie@example.com", "password123")

        user_profile = login_page.user_info
        username = login_page.username

        expect(user_profile).to_be_visible()
        expect(username).to_contain_text("charlie")

        user_profile.click()

        expect(login_page.user_name).to_be_visible()
        expect(login_page.user_mail).to_be_visible()
        expect(login_page.user_avatar).to_be_visible()
        expect(login_page.logout_btn).to_be_visible()

    @allure.title("test_logout")
    @allure.description("test_logout")
    @allure.tag("smoke")
    @pytest.mark.play
    def test_logout(self, page: Page):
        login_page = LoginPage(page)
        login_page.open()

        login_page.verify_page_opened()
        login_page.login("charlie@example.com", "password123")

        boards_page = BoardsPage(page)
        boards_page.open()

        login_page.user_info.click()

        login_page.logout_btn.click()

        login_page.verify_page_opened()
