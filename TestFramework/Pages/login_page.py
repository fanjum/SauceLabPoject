"""Implementing Login screen page objects"""

from selenium.webdriver.common.by import By

from TestFramework.Pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Contains Login UI page locators
    Login function
    Set user name on login page function
    """
    # Start: Login page locators
    user_name_input_field_locator = (By.ID, "user-name")
    password_input_field_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")

    # End: Login page locators

    def set_user_name(self, username):
        """
        Implementing set user name functionality
        :param username:
        :return:
        """
        self.set_value_into_intput_field(self.user_name_input_field_locator, username,
                                         'user name input field locator not found before specified time out')

    def set_password(self, password):
        """
        Implementing set password functionality
        :param password:
        :return:
        """
        self.set_value_into_intput_field(self.password_input_field_locator, password,
                                         'password input field locator not found before specified time out')

    def click_login_button(self):
        """
        Implementing set password functionality
        :return:
        """
        self.click(self.login_button_locator, 'login button locator not found before specified time out')
