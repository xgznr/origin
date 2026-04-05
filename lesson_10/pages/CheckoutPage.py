import allure
from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Заполнение формы заказа")
    def fill_form(self, first: str, last: str, zip_code: str) -> None:
        """
        Заполняем данные покупателя.
        :param first: Имя
        :param last: Фамилия
        :param zip_code: Почтовый индекс
        :return: None"""
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(
            By.ID, "postal-code").send_keys(zip_code)

        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой стоимости")
    def get_total_price(self) -> str:
        """
        Считывает текст финальной суммы
        :return: Строка с текстом суммы
        """
        return self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
            ).text
