import allure
from selenium.webdriver.common.by import By


class MainShopPage:

    def __init__(self, browser):
        self.driver = browser

    @allure.step("Авторизация пользователя")
    def login(self, user: str, pwd: str) -> None:
        """
        Выполняет вход в систему.
        :param user: Имя пользователя
        :param pwd: Пароль
        :return: None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(pwd)
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self, name: str) -> None:
        """
        Преобразуем название товара в id
        :param name: полное название товара
        :return: None
        """
        formatted_name = name.lower().replace(" ", "-")
        self.driver.find_element(
            By.ID, f"add-to-cart-{formatted_name}"
            ).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Кликает по иконке корзины
        :return: None
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "a[class='shopping_cart_link']"
            ).click()
