import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, browser):
        """
        Инициализация страницы корзины.
        :param browser: Экземпляр WebDriver.
        """
        self.driver = browser
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажать на кнопку оформления заказа (Checkout)")
    def checkout(self):
        """
        Выполняет переход из корзины к заполнению данных заказа.
        :return: None
        """
        self.driver.find_element(*self.checkout_button).click()
