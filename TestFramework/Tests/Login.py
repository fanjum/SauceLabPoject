"""Implementing Login functionality"""

from selenium.common.exceptions import WebDriverException


# from TestFramework.Pages.login_page import LoginPage
# from selenium.common.exceptions import WebDriverException
# from ..Helper.Logger import Logger
# from ..Pages.login_page import LoginPage

from TestFramework.Helper.Logger import Logger
from TestFramework.Pages.login_page import LoginPage


class Login:
    """
    Returning set user name on login page
    Returning set user name on login page
    Returning click login button status
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    logger = Logger().get_logger('Login')

    def __init__(self):
        self._login_page = LoginPage()

    def set_user_name(self, user_name):
        """
        Returning set user name status
        :param user_name:
        :return: True/False
        """
        status = None
        try:
            self.logger.info('Start: started set user name method')
            self._login_page.set_user_name(user_name)
            status = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            status = False
            raise
        finally:
            self.logger.info('End: set user name method')
            return status

    def set_password(self, password):
        """
        Returning set password status
        :param password:
        :return: True/False
        """
        status = None
        try:
            self.logger.info('Start: set password method')
            self._login_page.set_password(password)
            status = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            status = False
            raise
        finally:
            self.logger.info('End: set password method')
            return status

    def click_login_button(self):
        """
        Returning click login button status
        :return: True/False
        """
        is_clicked = None
        try:
            self.logger.info('Start: click saucelab login button method')
            self._login_page.click_login_button()
            is_clicked = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_clicked = False
            raise
        finally:
            self.logger.info('End: click saucelab login button method')
            return is_clicked

    def click_menu_button(self):
        """
        Returning click menu button status
        :return: True/False
        """
        is_clicked = None
        try:
            self.logger.info('Start: click menu button method')
            self._login_page.click_menu_button()
            is_clicked = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_clicked = False
            raise
        finally:
            self.logger.info('End: click menu button method')
            return is_clicked

    def click_logout_button(self):
        """
        Returning click logout button status
        :return: True/False
        """
        is_clicked = None
        try:
            self.logger.info('Start: click logout button method')
            self._login_page.click_logout_button()
            is_clicked = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_clicked = False
            raise
        finally:
            self.logger.info('End: click logout button method')
            return is_clicked
