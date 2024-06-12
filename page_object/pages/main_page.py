from page_object.pages.base_page import BasePage
from page_object.locators.main_pages_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step("Скролл до последнего вопроса")
    def scroll_to_questions(self, num):
        question_locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Получение текста ответа")
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)






