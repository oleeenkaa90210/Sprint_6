import allure
import pytest
from page_object.pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
            (1,
             'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
            (2,
             'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
            (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
            (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
            (5,
             'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
            (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
            # Comma added here
            (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
        ]
    )
    @allure.title('Тесты вопросы о важном')
    def test_questions_and_answers(self, driver, open_qa_scooter, num, result):
        main_page = MainPage(driver)
        main_page.scroll_to_questions(num)
        text = main_page.get_answer_text(num)
        assert text == result

        aria_disabled, aria_expanded = main_page.get_question_status(num)
        assert aria_disabled == 'true', f"Expected aria-disabled='true' but got {aria_disabled}"
        assert aria_expanded == 'true', f"Expected aria-expanded='true' but got {aria_expanded}"
