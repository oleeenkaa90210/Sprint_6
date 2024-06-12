from selenium.webdriver.common.by import By

class OrderPageLocators:

    ORDER_TOP_BUTTON = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC > button.Button_Button__ra12g")
    ORDER_BOTTOM_BUTTON = (By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm > button.Button_Button__ra12g.Button_Middle__1CSJM")
    NAME = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder='* Имя']")
    SURNAME = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH input[type='text'][placeholder='* Фамилия']")
    ADDRESS = (By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder='* Адрес: куда привезти заказ']")
    PHONE = (By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder='* Телефон: на него позвонит курьер']")
    METRO = (By.CSS_SELECTOR, "input.select-search__input[placeholder='* Станция метро']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "div.Order_NextButton__1_rCA button.Button_Button__ra12g.Button_Middle__1CSJM")
    METRO_STATION = (By.XPATH, "//div[contains(@class, 'Order_Text__2broi') and contains(text(), '{}')]")
    ORDER_TITLE = (By.CLASS_NAME, 'Order_Header__BZXOb')
    DATE_INPUT = (By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CSS_SELECTOR, ".Dropdown-control .Dropdown-placeholder")
    BACKGROUNG = (By.CLASS_NAME, 'App_App__15LM-')
    DROPDOWN_CONTROL = (By.CSS_SELECTOR, ".Dropdown-control")
    DROPDOWN_OPTION = (By.CSS_SELECTOR, ".Dropdown-menu .Dropdown-option")
    CHECKBOX = (By.CSS_SELECTOR, ".Checkbox_Input__14A2w")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Middle__1CSJM:not(.Button_Inverted__3IF-i)")
    YES_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[not(contains(@class, 'Button_Inverted__3IF-i')) and text()='Да']")
    CONFIRMATION_ORDER = (By.XPATH, "//div[contains(@class,'Order_ModalHeader__') and text()='Заказ оформлен']")
    CONFIRMATION_MODAL = (By.CLASS_NAME, 'Order_Modal__YZ-d3')


