import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper

BASE_URL = 'https://ok.ru/'
LOGIN_VALUE = 'mail@mail.ru'
PASSWORD_VALUE = '123'
ERROR_TEXT = 'Неправильно указан логин и/или пароль'

@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода к восстановлению после нескольких неудачных попыток авторизации')
def test_go_to_recovery_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_login(LOGIN_VALUE)
    LoginPage.input_password(PASSWORD_VALUE)
    LoginPage.click_login_button()
    assert LoginPage.get_error_text() == ERROR_TEXT
    for i in range(2):
        LoginPage.input_password(PASSWORD_VALUE)
        LoginPage.click_login_button()
    LoginPage.click_recovery()
    RecoveryPageHelper(browser)
