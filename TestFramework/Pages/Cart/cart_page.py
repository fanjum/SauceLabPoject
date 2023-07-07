"""Implementing cart screen page objects"""

from selenium.webdriver.common.by import By
from TestFramework.Pages.base_page import BasePage


class CartPage(BasePage):
    """
    Contains Cart UI page locators

    """
    # # Start: Cart page locators
    cart_icon_locator = (By.XPATH, "//span[@class='shopping_cart_badge']")
    checkout_button_locator = (By.ID, "checkout")
    first_name_locator = (By.ID, "first-name")
    last_name_locator = (By.ID, "last-name")
    zip_locator = (By.ID, "postal-code")

    # End: Cart page locators

    def click_cart_icon(self):
        """
        Implementing clicking on the cart icon functionality
        :param
        :return:
        """
        self.click(self.cart_icon_locator, 'Cart Icon locator not found before specified time out')

    def click_checkout_button(self):
        """
        Implementing clicking on the checkout button functionality
        :param
        :return:
        """
        self.click(self.checkout_button_locator, 'Checkout button locator not found before specified time out')

    def set_first_name(self, first_name):
        """
        Implementing set first name functionality
        :param first_name:
        :return:
        """
        self.set_value_into_intput_field(self.first_name_locator, first_name,
                                         'First name input field locator not found before specified time out')

    def set_last_name(self, last_name):
        """
        Implementing set last name functionality
        :param last_name:
        :return:
        """
        self.set_value_into_intput_field(self.last_name_locator, last_name,
                                         'Last name input field locator not found before specified time out')

    def set_zip(self, zip):
        """
        Implementing set zip functionality
        :param zip:
        :return:
        """
        self.set_value_into_intput_field(self.zip_locator, zip,
                                         'ZIP input field locator not found before specified time out')
