import allure
import random
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Выбор станции метро")
    def click_and_select_metro_station(self, station_name):
        self.click_to_element(OrderPageLocators.METRO)
        self.click_to_element(self.format_locators(OrderPageLocators.METRO_STATION, station_name))

    @allure.step("Клик на фон")
    def click_on_background(self):
        self.click_to_element(OrderPageLocators.BACKGROUNG)

    @allure.step("Клик и выбор периода аренды")
    def click_and_select_rental_period(self):
        self.click_to_element(OrderPageLocators.DROPDOWN_CONTROL)
        rental_periods = self.wait_all_element_located(OrderPageLocators.DROPDOWN_OPTION)
        random_index = random.randint(0, len(rental_periods) - 1)
        rental_periods[random_index].click()

    @allure.step("Выбор в чек-боксе")
    def select_random_checkbox(self):
        checkboxes = self.wait_all_element_located(OrderPageLocators.CHECKBOX)
        random_choice = random.choice(checkboxes)
        random_choice.click()

    @allure.step("Клик на верхнюю кнопку заказать")
    def click_on_top_button(self):
        self.click_to_element(OrderPageLocators.ORDER_TOP_BUTTON)

    @allure.step("Скролл до нижней кнопки заказать")
    def scroll_to_bottom_button(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BOTTOM_BUTTON)

    @allure.step("Клик на нижнюю кнопку заказать")
    def click_to_bottom_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BOTTOM_BUTTON)

    @allure.step("Ввод данных в поле Имя")
    def fill_name(self, name):
        self.add_text_to_element(OrderPageLocators.NAME, name)

    @allure.step("Ввод данных в поле Фамилия")
    def fill_surname(self, surname):
        self.add_text_to_element(OrderPageLocators.SURNAME, surname)

    @allure.step("Ввод данных в поле Адрес")
    def fill_address(self, address):
        self.add_text_to_element(OrderPageLocators.ADDRESS, address)

    @allure.step("Ввод данных в поле Телефон")
    def fill_phone(self, phone):
        self.add_text_to_element(OrderPageLocators.PHONE, phone)

    @allure.step("Клик на кнопку Далее")
    def click_to_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Дождаться заголовка заказа")
    def wait_order_title(self):
        self.find_element_with_wait(OrderPageLocators.ORDER_TITLE)

    @allure.step("Ввод данных в поле Дата")
    def fill_date(self, date):
        self.add_text_to_element(OrderPageLocators.DATE_INPUT, date)

    @allure.step("Клик на кнопку заказать")
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Клик на кнопку Да подтверждения заказа")
    def click_to_yes_button(self):
        self.click_to_element(OrderPageLocators.YES_BUTTON)

    @allure.step("Дождаться модального окна подтверждения")
    def wait_confirmation_modal(self):
        self.find_element_with_wait(OrderPageLocators.CONFIRMATION_MODAL)

    @allure.step("Получить текст модального окна подтверждения")
    def get_text_confirmation_modal(self):
        return self.get_text_from_element(OrderPageLocators.CONFIRMATION_ORDER)
