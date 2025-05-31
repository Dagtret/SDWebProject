from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '// *[ @ data - l = "t,sign_in"]')
    LOGIN_TAB = (By.XPATH, '// *[ @ data - l = "t,login_tab"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    QR_BUTTON = (By.XPATH, '// *[ @ data - l = "t,get_qr"]')
    QR_LOGIN_TAB = (By.XPATH, '// *[ @ data - l = "t,qr_tab"]')
    CANNOT_LOGIN_BUTTON = (By.XPATH, '// *[ @ data - l = "t,restore"]')
    REGISTER_BUTTON = (By.XPATH, '// *[ @ data - l = "t,register"]')
    VK_LOGIN_BUTTON = (By.XPATH, '// *[ @ class = "i ic social-icon __s __vk_id"]')
    MAIL_LOGIN_BUTTON = (By.XPATH, '// *[ @ class = "i ic social-icon __s __mailru"]')
    YANDEX_LOGIN_BUTTON = (By.XPATH, '// *[ @ class = "i ic social-icon __s __yandex"]')

class LoginPageHelper(BasePage):
    pass