from pages.Login_Page import LoginPage
import pytest
from config.config import TestData


# Login & LV-4828 https://smartpager.atlassian.net/browse/LV-4829
@pytest.mark.authentication
@pytest.mark.e2e
class TestLogin:
    def test_login_user_with_wrong_password(self):
        """  Login with wrong password """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.special_credentials_login(TestData.USER_NAME, "WrongPassword")
        self.loginPage.is_login_error_visible()
        self.loginPage.check_login_error_text()

    def test_forgot_options(self):
        """  Forgot password option """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.forgot_username(TestData.RECOVERY_EMAIL)
        self.loginPage.forgot_password(TestData.RECOVERY_EMAIL)

    def test_enterprise_login(self):
        """  Enterprise login """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enterpriseLogin(TestData.ENTERPRISE_SIGN_ON)
