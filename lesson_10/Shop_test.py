import pytest
import allure
from selenium import webdriver
from pages.MainShopPage import MainShopPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.title("Проверка итоговой суммы покупки")
@allure.description(
    "Тест проверяет корректность расчета Total Price при покупке трех товаров")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_purchase_total(driver):
    with allure.step("Открыть главную страницу"):
        driver.get("https://www.saucedemo.com/")

        login_page = MainShopPage(driver)
        login_page.login("standard_user", "secret_sauce")

        inv_page = MainShopPage(driver)
        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"
        ]
        for item in items:
            inv_page.add_to_cart(item)

        inv_page.go_to_cart()

        with allure.step("Переход к чекауту"):
            CartPage(driver).checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Evgenii", "Ivanov", "806800")

        with allure.step("Проверка итоговой суммы"):
            total_text = checkout_page.get_total_price()
            assert "58.29" in total_text, \
                f"Ожидалась сумма $58.29, но получили {total_text}"
