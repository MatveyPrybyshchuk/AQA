import pytest
from playwright.sync_api import Page, BrowserContext, expect


# '''
# Для 3 страниц описать PageObject, так чтобы в сумме было 6 тестов, на ваш проект

# 1 Login
# 2 Главная
# 3 все доски 
# 4 все задачи 
# Автотесты 
# 1 Отображение страниц
# 2 Авторизация 
# 3 Отображение информации о пользователе
# 4 Выход из приложения
# '''

# @pytest.mark.play
# def test_check(page: Page, context: BrowserContext):
#     page.goto("https://letcode.in/window")

#     page.locator('#multi').click()
    
#     all_pages = context.pages

#     new_pages = [p for p in all_pages if p != page]


#     expect(new_pages[0]).to_have_url("https://letcode.in/alert")
#     expect(new_pages[1]).to_have_url("https://letcode.in/dropdowns")

#     # new_page.wait_for_load_state("load", timeout=30000)
