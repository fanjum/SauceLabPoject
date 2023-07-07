"""Implementing Cart page functionality"""

from selenium.common.exceptions import WebDriverException
from TestFramework.Helper.Logger import Logger
from TestFramework.Pages.Inventory.inventory_page import InventoryPage
from TestFramework.Pages.Cart.cart_page import CartPage


class Cart:
    """
    Add products to cart
    Delete product from cart
    Add all products
    Sort by name
    Sort by price
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    logger = Logger().get_logger('Cart')

    def __init__(self):
        self._cart_page = CartPage()

    def click_cart_icon(self):
        """
        Returning click on the cart icon status
        :param:
        :return: True/False
        """
        is_added = None
        try:
            self.logger.info('Start: started clicking on the cart icon method')
            self._cart_page.click_cart_icon()
            is_added = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_added = False
            raise
        finally:
            self.logger.info('End: click on the cart icon method')
            return is_added

    def click_checkout_button(self):
        """
        Returning click on the checkout button
        :param:
        :return: True/False
        """
        is_added = None
        try:
            self.logger.info('Start: started clicking on the checkout method')
            self._cart_page.click_checkout_button()
            is_added = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_added = False
            raise
        finally:
            self.logger.info('End: click on the checkout method')
            return is_added

    def set_first_name(self, first_name):
        """
        Returning setting first name status
        :param:
        :return: True/False
        """
        is_added = None
        try:
            self.logger.info('Start: started setting first name method')
            self._cart_page.set_first_name(first_name)
            is_added = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_added = False
            raise
        finally:
            self.logger.info('End: setting first name method')
            return is_added

    def set_last_name(self, last_name):
        """
        Returning setting last name status
        :param:
        :return: True/False
        """
        is_added = None
        try:
            self.logger.info('Start: started setting last name method')
            self._cart_page.set_last_name(last_name)
            is_added = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_added = False
            raise
        finally:
            self.logger.info('End: setting last name method')
            return is_added

    def set_zip(self, zip):
        """
        Returning setting zip status
        :param:
        :return: True/False
        """
        is_added = None
        try:
            self.logger.info('Start: started setting zip method')
            self._cart_page.set_zip(zip)
            is_added = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_added = False
            raise
        finally:
            self.logger.info('End: setting zip method')
            return is_added
