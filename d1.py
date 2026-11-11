# ФИО: Волков М.А.
# Дата: 2026-11-11
# Время: 11:08
# код из написание тестов
import re
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Переход и проверка ссылки
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

    # Клик и проверка перехода сылки
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    
    browser.close()
