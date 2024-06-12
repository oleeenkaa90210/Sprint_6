import allure
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.support.wait import WebDriverWait
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage

class OrderPage(BasePage):
    @allure.step("Выбор станции метро")
    def click_and_select_metro_station(self, station_name):
        self.driver.find_element(*OrderPageLocators.METRO).click()
        l = self.format_locators(OrderPageLocators.METRO_STATION, station_name)
        el = self.driver.find_element(*l)

        el.click()

    @allure.step("Клик на фон")
    def click_on_background(self):
        self.driver.find_element(*OrderPageLocators.BACKGROUNG).click()

    @allure.step("Клик и выбор периода аренды")
    def click_and_select_rental_period(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((OrderPageLocators.DROPDOWN_CONTROL))).click()
        rental_periods = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(OrderPageLocators.DROPDOWN_OPTION)
        )
        random_index = random.randint(0, len(rental_periods) - 1)
        rental_periods[random_index].click()

    @allure.step("Выбор в чек-боксе")
    def select_random_checkbox(self):
        checkboxes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((OrderPageLocators.CHECKBOX))
        )
        random_choice = random.choice(checkboxes)
        random_choice.click()

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, element):
        element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)





















