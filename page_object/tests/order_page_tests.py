import allure
import pytest
from page_object.helpers import generate_order_info
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.moving_to_page import MovingPage
from page_object.pages.order_page import OrderPage


class TestOrderPage():

    @pytest.mark.parametrize("user_info", [
        generate_order_info(),
        generate_order_info()
    ])
    @allure.description('Создание заказа с верхней кнопки Заказать')
    def test_create_order_from_top_order_button(self, driver, open_qa_scooter, user_info):
        order_page = OrderPage(driver)
        moving_page = MovingPage(driver)
        order_page.find_element_with_wait(OrderPageLocators.ORDER_TOP_BUTTON)
        order_page.click_to_element(OrderPageLocators.ORDER_TOP_BUTTON)
        text = self.create_order(order_page, moving_page, user_info)


        assert "Заказ оформлен" in text

    @pytest.mark.parametrize("user_info", [
            generate_order_info(),
            generate_order_info()
    ])
    @allure.description('Создание заказа с нижней кнопки Заказать')
    def test_create_order_from_bottom_order_button(self, driver, open_qa_scooter, user_info):
        order_page = OrderPage(driver)
        moving_page = MovingPage(driver)
        order_page.scroll_to_element(OrderPageLocators.ORDER_BOTTOM_BUTTON)
        order_page.find_element_with_wait(OrderPageLocators.ORDER_BOTTOM_BUTTON)
        order_page.click_to_element(OrderPageLocators.ORDER_BOTTOM_BUTTON)
        text = self.create_order(order_page, moving_page, user_info)

        assert "Заказ оформлен" in text

    def create_order(self, order_page, moving_page, user_info):
        order_page.add_text_to_element(OrderPageLocators.NAME, user_info['name'])
        order_page.add_text_to_element(OrderPageLocators.SURNAME, user_info['surname'])
        order_page.add_text_to_element(OrderPageLocators.ADDRESS, user_info['address'])
        order_page.click_and_select_metro_station(user_info['metro'])
        order_page.add_text_to_element(OrderPageLocators.PHONE, user_info['phone'])
        order_page.click_to_element(OrderPageLocators.NEXT_BUTTON)
        moving_page.find_element_with_wait(OrderPageLocators.ORDER_TITLE)
        order_page.add_text_to_element(OrderPageLocators.DATE_INPUT, user_info['date'])
        order_page.click_on_background()
        order_page.click_and_select_rental_period()
        order_page.select_random_checkbox()
        order_page.click_to_element(OrderPageLocators.ORDER_BUTTON)
        order_page.find_element_with_wait(OrderPageLocators.YES_BUTTON)
        order_page.click_to_element(OrderPageLocators.YES_BUTTON)
        order_page.find_element_with_wait(OrderPageLocators.CONFIRMATION_MODAL)
        return order_page.get_text_from_element(OrderPageLocators.CONFIRMATION_ORDER)

