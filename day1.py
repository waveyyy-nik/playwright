# ФИО: Никулина Виктория Евгеньевна
# Дата: 10.11.2026
# Время: 13:43
# Описание: Этот код запускает браузер Chromium, открывает страницу
# playwright.dev и выводит заголовок страницы в консоль.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    browser.close()