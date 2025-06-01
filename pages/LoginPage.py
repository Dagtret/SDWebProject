from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_TAB = (By.XPATH, '// *[@data-l="t,login_tab"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    QR_LOGIN_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    CANNOT_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTER_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/*[@data-l="t,register"]')
    VK_LOGIN_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    MAIL_LOGIN_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    YANDEX_LOGIN_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    ERROR_TEXT = (By.XPATH,'//*[@class="input-e login_error"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.QR_LOGIN_TAB)
        self.find_element(LoginPageLocators.CANNOT_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.VK_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.MAIL_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_LOGIN_BUTTON)

    def click_login_button(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    def click_login_field(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).click()

    def input_login(self, value):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(value)
