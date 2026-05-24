import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.title("Успешный вход в систему")
@allure.description("Проверяем, что с правильными логином и паролем происходит вход и отображается сообщение об успехе")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    flash = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in flash

@allure.title("Неуспешный вход с неверными данными")
@allure.description("Проверяем, что при вводе неправильных логина и пароля появляется сообщение об ошибке")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.NORMAL)
def test_unsuccessful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    flash = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in flash