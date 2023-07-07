"""Implementing cart screen page objects"""

from selenium.webdriver.common.by import By
from TestFramework.Pages.base_page import BasePage


class CartPage(BasePage):
    """
    Contains Cart UI page locators

    """
    # # Start: Cart page locators
    cart_icon_locator = (By.XPATH, "//span[@class='shopping_cart_badge']")

    # End: Cart page locators

    def click_cart_icon(self):
        """
        Implementing clicking on the cart icon functionality
        :param
        :return:
        """
        self.click(self.cart_icon_locator, 'Cart Icon locator not found before specified time out')
