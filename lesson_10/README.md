Автоматизированные тесты для проверки функционала покупки на сайте [SauceDemo](https://saucedemo.com).

## Требования
1. Python 3.x
2. Установленный Geckodriver (для Firefox) или Chromedriver.
3. Установленный [Allure Commandline](https://qameta.io).

## Установка зависимостей
```bash
pip install pytest selenium allure-pytest

## Команды
Как запустить тесты: pytest --alluredir=allure-results
Как посмотреть отчет: allure serve allure-results