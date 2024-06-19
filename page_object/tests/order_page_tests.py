import allure
import pytest
from page_object.helpers import generate_order_info
from page_object.pages.order_page import OrderPage


def create_order(order_page, user_info):
    order_page.fill_name(user_info['name'])
    order_page.fill_surname(user_info['surname'])
    order_page.fill_address(user_info['address'])
    order_page.click_and_select_metro_station(user_info['metro'])
    order_page.fill_phone(user_info['phone'])
    order_page.click_to_next_button()
    order_page.wait_order_title()
    order_page.fill_date(user_info['date'])
    order_page.click_on_background()
    order_page.click_and_select_rental_period()
    order_page.select_random_checkbox()
    order_page.click_to_order_button()
    order_page.click_to_yes_button()
    order_page.wait_confirmation_modal()

    return order_page.get_text_confirmation_modal()


class TestOrderPage:

    @pytest.mark.parametrize("user_info", [
        generate_order_info(),
        generate_order_info()
    ])
    @allure.title('Создание заказа с верхней кнопки Заказать')
    def test_create_order_from_top_order_button(self, driver, open_qa_scooter, user_info):
        order_page = OrderPage(driver)
        order_page.click_on_top_button()
        text = create_order(order_page, user_info)

        assert "Заказ оформлен" in text

    @pytest.mark.parametrize("user_info", [
            generate_order_info(),
            generate_order_info()
    ])
    @allure.title('Создание заказа с нижней кнопки Заказать')
    def test_create_order_from_bottom_order_button(self, driver, open_qa_scooter, user_info):
        order_page = OrderPage(driver)
        order_page.scroll_to_bottom_button()
        order_page.click_to_bottom_button()
        text = create_order(order_page, user_info)

        assert "Заказ оформлен" in text

