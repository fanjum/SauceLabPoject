"""Implementing Login functionality"""

from selenium.common.exceptions import WebDriverException
from TestFramework.Helper.Logger import Logger
from TestFramework.Pages.Inventory.inventory_page import InventoryPage


class Inventory:
    """
    Add products to cart
    Delete product from cart
    Add all products
    Sort by name
    Sort by price
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    logger = Logger().get_logger('Login')

    def __init__(self):
        self._inventory_page = InventoryPage()

    def add_a_product_to_cart(self, product_name, product_page):
        """
        Returning add a product to cart status
        :param product_name:
        :return: True/False
        """
        is_added = None
        try:
            self.logger.info('Start: started add a product to cart method')
            self._inventory_page.add_a_product_to_cart(product_name, product_page)
            is_added = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_added = False
            raise
        finally:
            self.logger.info('End: add a product to cart method')
            return is_added

    def remove_a_product_to_cart(self, product_name, product_page):
        """
        Returning remove a product to cart status
        :param product_name:
        :return: True/False
        """
        is_removed = None
        try:
            self.logger.info('Start: started remove a product to cart method')
            self._inventory_page.remove_a_product_to_cart(product_name, product_page)
            is_removed = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_removed = False
            raise
        finally:
            self.logger.info('End: remove a product to cart method')
            return is_removed

    def sort(self, sort_criteria):
        """
        Returning sorting by name status
        :param sort_criteria
        :return: True/False
        """
        is_sorted = None
        try:
            self.logger.info('Start: started sorting method')
            self._inventory_page.sort(sort_criteria)
            is_sorted = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_sorted = False
            raise
        finally:
            self.logger.info('End: sorting method')
            return is_sorted
