import allure

from page_object.locators.moving_to_page_locators import MovingPageLocators
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.moving_to_page import MovingPage
from page_object.pages.order_page import OrderPage


class TestMovingPage:
    @allure.description('Клик на логотип яндекс')
    def test_click_on_logo_yandex(self, driver, open_qa_scooter):
        moving_page = MovingPage(driver)
        moving_page.click_to_element(MovingPageLocators.LOGO_YANDEX)
        moving_page.switch_to_new_window()
        moving_page.wait_new_window_url()

        expected_url = 'https://dzen.ru/?yredirect=true'
        assert driver.current_url == expected_url, f'URL нового окна {driver.current_url} не соответствует ожидаемому {expected_url}'

    @allure.description('Клик на логотип самокат')
    def test_click_on_logo_samokat(self, driver, open_qa_scooter):
        moving_page = MovingPage(driver)
        order_page = OrderPage(driver)
        order_page.find_element_with_wait(OrderPageLocators.ORDER_TOP_BUTTON)
        order_page.click_to_element(OrderPageLocators.ORDER_TOP_BUTTON)

        moving_page.click_to_element(MovingPageLocators.LOGO_SAMOKAT)
        moving_page.wait_for_main_page()

        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", f'URL {driver.current_url} не соответствует ожидаемому https://qa-scooter.praktikum-services.ru/'





