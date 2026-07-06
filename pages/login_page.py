from playwright.sync_api import Page, expect

from core.base_page import BasePage


class LoginPage(BasePage):

    path = '/login'
    title = 'Task Management Board'

    def __init__(self, page: Page):
        super().__init__(page)

        self.form_container = page.locator('.hero.hero--home.auth-form-container')
        self.section_title = page.get_by_role('heading', name='Вход в систему', exact=True)
        self.link_registrate = page.get_by_role('link', name='зарегистрируйтесь', exact=True)

        self.inputfield_email = page.locator('#id-input-login-email-input')
        self.inputfield_password = page.locator('#id-input-login-password-input')
        self.btn_enter = page.locator('.btn.btn-primary.btn-md.w-full')

    def open(self) -> None:
        self.goto(self.path)

    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.form_container).to_be_visible()
        expect(self.section_title).to_be_visible()
        expect(self.link_registrate).to_be_visible()

        expect(self.inputfield_email).to_be_editable()
        expect(self.inputfield_password).to_be_editable()
        expect(self.btn_enter).to_be_enabled()

    def login(self, email, password) -> None:
        self.inputfield_email.fill(email)
        self.inputfield_password.fill(password)
        self.btn_enter.click()
