import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Форматирование локатора")
    def format_locators(self, locator_template, num):
        locator_type, locator_string = locator_template
        formatted_locator = locator_string.format(num)
        return locator_type, formatted_locator

    @allure.step("Найти элемент и подождать")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Клик на элемент")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Получение всех элементов")
    def wait_all_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))


    @allure.step("Добавление текса в элемент")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Ожидание нового url")
    def wait_to_new_url(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step("Текущий url")
    def current_page(self):
        return self.driver.current_url

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Открытие нового окна")
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        new_window = [window for window in windows if window != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_window)

