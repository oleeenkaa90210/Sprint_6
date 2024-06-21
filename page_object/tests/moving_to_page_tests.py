import allure
from page_object.data import Urls
from page_object.pages.moving_to_page import MovingPage


class TestMovingPage:
    @allure.title('Клик на логотип яндекс')
    def test_click_on_logo_yandex(self, driver, open_qa_scooter):
        moving_page = MovingPage(driver)
        moving_page.click_to_logo_yandex()
        moving_page.switch_to_new_window()
        moving_page.wait_new_window_dzen()

        assert moving_page.current_page() == Urls.DZEN, f'URL нового окна {moving_page.current_page()} не соответствует ожидаемому {Urls.DZEN}'

    @allure.title('Клик на логотип самокат')
    def test_click_on_logo_samokat(self, driver, open_qa_scooter):
        moving_page = MovingPage(driver)
        moving_page.click_on_top_button()

        moving_page.click_on_logo_samokat()
        moving_page.wait_for_main_page()

        assert moving_page.current_page() == Urls.MAIN_PAGE, f'URL {moving_page.current_page()} не соответствует ожидаемому {Urls.MAIN_PAGE}'





