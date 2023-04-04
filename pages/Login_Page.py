import time
import yaml
from selenium.webdriver.common.by import By
from shared_components.SharedActions import MainPage
from logs.logging_setup import LoggingSetup
from concurrent.futures import ThreadPoolExecutor


class LoginPage(MainPage):
    # Class constructor
    def __int__(self, driver):
        super().__init__(driver)

    # Page Locators
    EMAIL_FIELD = (By.NAME, "txtUserName")
    PASSWORD_FIELD = (By.NAME, "txtUserPass")
    SIGN_IN_BUTTON = (By.XPATH, "//input[contains(@value,'Sign in')]")
    LOGIN_ERROR = (By.ID, "errorDiv")
    FORGOT_USERNAME = (By.ID, "forgotUsernameAnchor")
    RECOVERY_EMAIL = (By.NAME, "txtEmail")
    BACK_LOGIN = (By.XPATH, "//a[contains(.,'Back to the login page')]")
    FORGOT_PASSWORD = (By.ID, "forgotPasswordAnchor")
    SUBMIT = (By.ID, "cmdSubmit")
    ENTERPRISE_BUTTON = (By.XPATH, "//a[contains(.,'Enterprise Login')]")
    IDENTIFIER = (By.XPATH, "//input[contains(@placeholder,'Identifier')]")

    log = LoggingSetup.sample_logger()

    # Page actions - Methods

    def special_credentials_login(self, email, password):
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.login_function()

    def login_function(self):
        self.is_element_visible(self.SIGN_IN_BUTTON)
        self.click_element(self.SIGN_IN_BUTTON)
        self.log.info("User is logging in")

    def is_login_error_visible(self):
        self.is_element_visible(self.LOGIN_ERROR)
        self.log.info("Error visible")

    def check_login_error_text(self):
        error_text = self.get_element_text(self.LOGIN_ERROR)
        assert error_text == \
               "* Unable to validate your user account. Please note that both the username and password are case-sensitive."

    def forgot_username(self, email):
        self.click_element(self.FORGOT_USERNAME)
        self.send_keys(self.RECOVERY_EMAIL, email)
        self.click_element(self.BACK_LOGIN)

    def forgot_password(self, email):
        self.click_element(self.FORGOT_PASSWORD)
        self.send_keys(self.RECOVERY_EMAIL, email)
        self.click_element(self.SUBMIT)

    def enterpriseLogin(self, enterprise_sign_on):
        self.click_element(self.ENTERPRISE_BUTTON)
        self.send_keys(self.IDENTIFIER, enterprise_sign_on)
        self.click_element(self.SIGN_IN_BUTTON)
