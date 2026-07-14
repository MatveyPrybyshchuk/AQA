import pytest, allure
from playwright.sync_api import Page, expect
from pages.subscription_page import SubscriptionPage

@allure.feature("Subscription Page")
class TestSubscriptionPage:
    @allure.title("test_open_subscription_page")
    @allure.description("test_open_subscription_page")
    @allure.tag("smoke")
    @pytest.mark.subs
    def test_open_subscription_page(self, page: Page):
        subscription_page = SubscriptionPage(page)
        subscription_page.open()
        subscription_page.verify_page_opened()

    @allure.title("test_period_selector")
    @allure.description("test_period_selector")
    @allure.tag("smoke")
    @pytest.mark.parametrize("months, tariff", [
        (1, "basic"),
        (1, "premium"),
        (1, "family"),
        (3, "basic"),
        (3, "premium"),
        (3, "family"),
        (12, "basic"),
        (12, "premium"),
        (12, "family"),
    ])
    @pytest.mark.subs
    def test_period_selector(self, page: Page, months: int, tariff: str):
        subscription_page = SubscriptionPage(page)
        subscription_page.open()
        subscription_page.verify_page_opened()

        subscription_page.select_period(months)
        subscription_page.select_subs(tariff)
        subscription_page.check_selected_period_ans_subs(months, tariff)
