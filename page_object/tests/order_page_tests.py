import allure
import pytest
from page_object.helpers import generate_order_info
from page_object.pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize("user_info", [
        generate_order_info(),
        generate_order_info()
    ])
    @allure.title('Создание заказа с верхней кнопки Заказать')
    def test_create_order_from_top_order_button(self, driver, open_qa_scooter, user_info):
        order_page = OrderPage(driver)
        order_page.click_on_top_button()
        text = order_page.create_order(user_info)

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
        text = order_page.create_order(user_info)

        assert "Заказ оформлен" in text

