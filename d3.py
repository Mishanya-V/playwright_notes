# ФИО: Волков М.А.
# Дата: 2026-12-11
# Время: 16:17
# 1 тест проверяет наличие слова Playwright в заголовке страницы, а 2 тест кликает по ссылке "Get started" и убеждается, что открылась страница "Installation"
import re
from playwright.sync_api import Page, expect

def test_homepage_has_Playwright_in_title(page: Page):
    # Проверяет наличие слова Playwright в заголовке главной страницы
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    #Проверяет переход по ссылке Get started на страницу Installation
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()