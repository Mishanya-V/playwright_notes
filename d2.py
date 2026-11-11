# ФИО: Волков М.А.
# Дата: 2026-11-11
# Время: 17:00
# Я использовал Codegen, чтобы он сам написал заготовку кода. Он запускает браузер и создает изолированный контекст для теста. Код взят из генераций тестов. Также редакитрировал код в нем в соответствии с интркуцией

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
