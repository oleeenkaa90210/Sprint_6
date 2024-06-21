import allure
from page_object.data import Urls
from page_object.locators.moving_to_page_locators import MovingPageLocators
from page_object.pages.base_page import BasePage


class MovingPage(BasePage):

    @allure.step("Ожидание перехода на главную страницу")
    def wait_for_main_page(self):
        self.wait_to_new_url(Urls.MAIN_PAGE)

    @allure.step("Открытие нового окна Dzen")
    def wait_new_window_dzen(self):
        self.wait_to_new_url(Urls.DZEN)

    @allure.step("Клик на лого Яндекс")
    def click_to_logo_yandex(self):
        self.click_to_element(MovingPageLocators.LOGO_YANDEX)

    @allure.step("Клик на верхнюю кнопку заказать")
    def click_on_top_button(self):
        self.click_to_element(MovingPageLocators.ORDER_TOP_BUTTON)

    @allure.step("Клик на лого самокат")
    def click_on_logo_samokat(self):
        self.click_to_element(MovingPageLocators.LOGO_SAMOKAT)



