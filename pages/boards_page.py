from playwright.sync_api import Page, expect

from core.base_page import BasePage


class BoardsPage(BasePage):

    path = '/boards'
    title = 'Task Management Board'

    def __init__(self, page: Page):
        super().__init__(page)

        self.boards_page = page.locator('[data-qa="boards-page"]')

        self.page_title = page.locator('.brand-title')
        self.page_subtitle = page.locator('.brand-subtitle')
        self.userinfo = page.locator('.header-user-info')

        self.sidebar_nav = page.locator('.sidebar-nav')
        self.sidebar_homelink = page.locator('[data-qa="sidebar-home-link"]')
        self.sidebar_boardslink = page.locator('[data-qa="sidebar-boards-link"]')
        self.sidebar_taskslink = page.locator('[data-qa="sidebar-tasks-link"]')

        self.btn_create_dash = page.locator('.btn.btn-primary.btn-md')
        self.filter_form = page.locator('[data-qa="boards-filters"]')

        self.all_boards = page.locator('.card.mb-6')

        # dashboard creation
        self.dashname = page.locator('#id-input-create-board-title-input')
        self.description = page.locator('.textarea-modern ')
        self.checkbox_publicdash = page.locator('.checkbox-label')
        self.btn_create_dashboard = page.locator('.btn.btn-primary.btn-md')
    
    def open(self) -> None:
        self.goto(self.path)

    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.boards_page).to_be_visible()

    def verify_empty_state(self) -> None:
        expect(self.page_title).to_have_text('Task Management System')
        expect(self.page_subtitle).to_contain_text('Система управления задачами')
        expect(self.userinfo).to_be_visible()

        expect(self.sidebar_nav).to_be_visible()
        expect(self.sidebar_homelink).to_be_visible()
        expect(self.sidebar_boardslink).to_be_visible()
        expect(self.sidebar_taskslink).to_be_visible()

        expect(self.btn_create_dash).to_have_text("Создать доску")
        expect(self.filter_form).to_be_visible()

        expect(self.all_boards).to_be_visible()

    def create_dashboard(self, dashboardname='', description='', public=False):
        self.btn_create_dash.click()
        self.dashname.fill(dashboardname)
        self.dashname.fill(description)
        if public: 
            self.checkbox_publicdash.check()
        self.btn_create_dashboard.click()
