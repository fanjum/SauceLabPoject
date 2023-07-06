"""Implementing Login screen page objects"""

from selenium.webdriver.common.by import By
from TestFramework.Pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Contains Products UI page locators
    Add function
    Remove function
    Price sort function
    Name sort function
    """
    # # Start: Inventory page locators
    product_add_button_locator = (
        By.XPATH, "//div[@class='inventory_item_name' and normalize-space()='{}']/ancestor::div["
                  "@class='inventory_item']/descendant::button[@class='btn btn_primary btn_small "
                  "btn_inventory']")
    product_remove_button_locator = (
        By.XPATH, "//div[@class='inventory_item_name' and normalize-space()='{}']/ancestor::div["
                  "@class='inventory_item']/descendant::button[@class='btn btn_secondary btn_small "
                  "btn_inventory']")

    product_item_locator = (By.XPATH, "//div[@class='inventory_item_name' and normalize-space()='{}']")
    product_page_add_button_locator = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")
    product_page_remove_button_locator = (By.XPATH, "//button[@class='btn btn_secondary btn_small btn_inventory']")
    sort_name_az_locator = (By.XPATH, "//option[contains(normalize-space(),'Name (A to Z)')]")
    products_locator = (By.XPATH, "//div[@class='inventory_item_name']")

    # End: Inventory page locators

    def add_a_product_to_cart(self, product_name, product_page):
        """
        Implementing add a product to cart functionality
        :param product_name:
        :return:
        """
        if product_page:
            # Update the product_item_locator with the product_name
            self.product_item_locator = (
                self.product_item_locator[0], self.product_item_locator[1].format(product_name))
            # Click on the product using the updated locator.
            self.click(self.product_item_locator, 'Product item locator not found before specified time out')
            # Click on the add to cart button on the product page.
            self.click(self.product_page_add_button_locator,
                       'Product add button locator not found before specified time out')
        else:
            # Update the product_add_button_locator with the product_name
            self.product_add_button_locator = (
                self.product_add_button_locator[0], self.product_add_button_locator[1].format(product_name))
            # Click on the button using the updated locator
            self.click(self.product_add_button_locator,
                       'Product add button locator not found before specified time out')

    def remove_a_product_to_cart(self, product_name, product_page):
        """
        Implementing remove the product from cart functionality
        :param product_name:
        :return:
        """
        if product_page:
            # Click on the add to cart button on the product page.
            self.click(self.product_page_remove_button_locator,
                       'Product add button locator not found before specified time out')
        else:
            # Update the product_remove_button_locator with the product_name
            self.product_remove_button_locator = (
                self.product_remove_button_locator[0], self.product_remove_button_locator[1].format(product_name))

            # Click on the button using the updated locator
            self.click(self.product_remove_button_locator,
                       'Product remove button locator not found before specified time out')

    def sort_name_az(self):
        """
        Implementing sort by name functionality
        :return:
        """
        # Click on the Name A to Z from dropdown
        self.click(self.sort_name_az_locator, 'Sort Name A to Z locator not found before specified time out')

        # Retrieve the list of product names
        product_name_elements = self.find_elements(self.products_locator)
        product_names = [element.text for element in product_name_elements]

        # Create a sorted copy of the product names list
        sorted_names = sorted(product_names)

        # Compare the original list with the sorted list
        is_sorted = product_names == sorted_names
        return is_sorted

    # def click_login_button(self):
    #     """
    #     Implementing set password functionality
    #     :return:
    #     """
    #     self.click(self.login_button_locator, 'login button locator not found before specified time out')
