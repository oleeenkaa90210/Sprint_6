from page_object.pages.base_page import BasePage
from page_object.locators.main_pages_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step("Скролл до последнего вопроса")
    def scroll_to_questions(self, num):
        question_locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(question_locator)

    @allure.step("Получение текста ответа")
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Получение статуса вопроса")
    def get_question_status(self,num):
        question_locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)

        element = self.find_element_with_wait(question_locator)
        aria_disabled = element.get_attribute('aria-disabled')
        aria_expanded = element.get_attribute('aria-expanded')

        return aria_disabled,aria_expanded









