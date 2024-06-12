import allure
from page_object.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MovingPage(BasePage):
    @allure.step("Открытие нового окна")
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        new_window = [window for window in windows if window != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_window)

    @allure.step("Ожидание перехода на главную страницу")
    def wait_for_main_page(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/"))

    @allure.step("Открытие нового окна")
    def wait_new_window_url(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://dzen.ru/?yredirect=true'))




