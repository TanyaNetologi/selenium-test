# Selenium UI Tests

Учебный проект по автоматизированному тестированию веб-интерфейса с использованием Python, Selenium и Pytest.

## Что тестируется

Тесты выполняются для страницы авторизации The Internet.

Реализованы сценарии:

- успешная авторизация с валидными данными;
- неуспешная авторизация с неверными данными;
- проверка сообщения об успешном входе;
- проверка сообщения об ошибке авторизации.

## Технологии

- Python
- Selenium WebDriver
- Pytest
- Allure
- GitHub Actions

## Запуск тестов

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить тесты:

```bash
pytest
```

Для формирования результатов Allure:

```bash
pytest --alluredir=allure-results
```

Для просмотра Allure-отчёта:

```bash
allure serve allure-results
```

## CI

Автоматический запуск тестов настроен с помощью GitHub Actions.
