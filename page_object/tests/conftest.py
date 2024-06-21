import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def open_qa_scooter(driver):
    driver.get("https://qa-scooter.praktikum-services.ru/")
