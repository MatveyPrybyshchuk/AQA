from typing import Literal
import allure

from playwright.sync_api import Page, expect
from core.base_page import BasePage


class SubscriptionPage(BasePage):

    PERIOD_NAMES = {
        1: "basic",
        3: "premium",
        12: "family"
    }

    path = '/automation-lab/subscription'
    title = 'Task Management Board'

    def __init__(self, page: Page):
        super().__init__(page)

        self.subscription_hero = page.locator('.subscription-hero')
        self.period_section = page.locator('.period-section')
        self.tariffs_section = page.locator('.tariffs-section')
        self.promo_section = page.locator('.promo-section')
        self.payment_section = page.locator('.payment-section')
        self.summary_section = page.locator('.summary-section')
        self.pay_btn = page.locator('.pay-button')
        self.pay_btn_old_price = page.locator('.pay-btn-old-price')
        self.pay_btn_price = page.locator('.pay-btn-price')

    def open(self) -> None:
        self.goto(self.path)

    def verify_page_opened(self, url = None, title = None) -> None:
        expect(self.subscription_hero).to_be_visible()
        expect(self.period_section).to_be_visible()
        expect(self.tariffs_section).to_be_visible()
        expect(self.promo_section).to_be_visible()
        expect(self.payment_section).to_be_visible()
        expect(self.summary_section).to_be_visible()

    @allure.step("select_period by UI")
    def select_period(self, months: Literal[1, 3, 12]):
        period = self.page.locator(f'[data-testid="period-{months}"]')
        period.click()

    @allure.step("select_subscription by UI")
    def select_subs(self, tariff):
        period = self.page.locator(f'[data-testid="tariff-{tariff}"]')
        period.click()

    @allure.step("check_selected_period_ans_subs by UI")
    def check_selected_period_ans_subs(self, months: int, tariff):
        price_per_month = {"basic": 299, "premium": 499, "family": 799}
        discount = {1: 1, 3: 0.9, 12: 0.5}

        tariffs = {"basic": "Базовый", "premium": "Премиум", "family": "Семейный"}
        period = {1: "1 месяц", 3: "3 месяца", 12: "12 месяцев"}

        for tariff_check in ["basic", "premium", "family"]:
            total_price = int(price_per_month[tariff_check] * discount[months] * months)

            formatted_price = f"{total_price:,}".replace(",", " ")

            expected_text = None
            if months == 1:
                expected_text = "Оплата ежемесячно"
            elif months == 3:
                expected_text = f"При оплате {formatted_price} ₷ раз в 3 месяца"
            elif months == 12:
                expected_text = f"При оплате {formatted_price} ₷ раз в 12 месяцев"

            loc_total_price_label = self.page.locator(f'[data-tariff="{tariff_check}"] .total-label')
            loc_period_badge = self.page.locator(f'[data-tariff="{tariff_check}"] .tariff-period-badge')
            loc_tariff = self.page.locator("//span[@class='summary-label' and text()='Тариф']/following-sibling::span[@class='summary-value']")
            loc_period = self.page.locator("//span[@class='summary-label' and text()='Период']/following-sibling::span[@class='summary-value']")
            loc_discount = self.page.locator("//span[@class='summary-value discount']")
            loc_savings = self.page.locator("//span[@class='summary-label' and text()='Экономия']/following-sibling::span[@class='summary-value']")

            expect(loc_total_price_label).to_have_text(expected_text)
            expect(loc_period_badge).to_have_text(f"{str(months)}")

        expect(loc_tariff).to_have_text(f"{tariffs[tariff]}")
        expect(loc_period).to_have_text(f"{period[months]}")

        old_price = price_per_month[tariff] * months
        new_price = int(price_per_month[tariff] * discount[months] * months)

        discount = old_price - new_price
        formatted_old_price = f"{old_price:,}".replace(",", " ")
        formatted_new_price = f"{new_price:,}".replace(",", " ")
        formatted_discount = f"{discount:,}".replace(",", " ")

        if months != 1:
            expect(loc_discount).to_have_text(f"-{formatted_discount} ₷")
            expect(loc_savings).to_have_text(f"{formatted_discount} ₷")

            expect(self.pay_btn_old_price).to_have_text(formatted_old_price)
            expect(self.pay_btn_price).to_have_text(formatted_new_price)
