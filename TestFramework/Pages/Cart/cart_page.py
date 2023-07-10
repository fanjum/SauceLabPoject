"""Implementing cart screen page objects"""

from selenium.webdriver.common.by import By
from TestFramework.Pages.base_page import BasePage


class CartPage(BasePage):
    """
    Contains Cart UI page locators

    """
    # # Start: Cart page locators
    cart_icon_locator = (By.XPATH, "//span[@class='shopping_cart_badge']")
    item_name_locator = (By.XPATH, "//div[@class='inventory_item_name']")
    checkout_button_locator = (By.ID, "checkout")
    first_name_locator = (By.ID, "first-name")
    last_name_locator = (By.ID, "last-name")
    zip_locator = (By.ID, "postal-code")
    continue_button_locator = (By.ID, "continue")
    finish_button_locator = (By.ID, "finish")
    confirmation_message_locator = (By.XPATH, "//h2[@class = 'complete-header']")

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

    def click_continue_button(self):
        """
        Implementing clicking on the continue button functionality
        :param
        :return:
        """
        self.click(self.continue_button_locator, 'Continue button locator not found before specified time out')

    def click_finish_button(self):
        """
        Implementing clicking on the finish button functionality
        :param
        :return:
        """
        self.click(self.finish_button_locator, 'Finish button locator not found before specified time out')

    def verify_selected_items_count(self):
        """
        Implementing verify selected items count functionality
        :param
        :return:
        """
        # Retrieve the cart icon element
        items_no_element = self.find_element(self.cart_icon_locator)

        # Extract the displayed count from the cart icon element and convert it to an integer
        items_no = int(items_no_element.text)

        # Get the list of remove buttons and calculate the count
        element_elements = self.find_elements(self.item_name_locator)
        element_count = len(element_elements)

        # Compare the counts of selected items and displayed items in the cart
        is_correct = items_no == element_count

    def validate_confirmation_message(self, expected_text):
        """
        Implementing verify confirmation message functionality
        :param expected_text
        :return:
        """
        confirmation_message_text = self.find_element(self.confirmation_message_locator).text
        assert expected_text in confirmation_message_text, "Confirmation message does not contain the provided test"
