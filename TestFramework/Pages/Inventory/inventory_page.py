"""Implementing Inventory screen page objects"""

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
    product_add_button_locator = (By.XPATH,
                                  "//div[@class='inventory_item_name' and text()='{}']/ancestor::div[@class='inventory_item']/descendant::button[@class='btn btn_primary btn_small btn_inventory']")
    product_remove_button_locator = (By.XPATH,
                                     "//div[@class='inventory_item_name' and text()='{}']/ancestor::div[@class='inventory_item']/descendant::button[@class='btn btn_secondary btn_small btn_inventory']")
    product_item_locator = (By.XPATH, "//div[@class='inventory_item_name' and normalize-space()='{}']")
    product_page_add_button_locator = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")
    product_page_remove_button_locator = (By.XPATH, "//button[@class='btn btn_secondary btn_small btn_inventory']")
    sort_name_az_locator = (By.XPATH, "//option[contains(normalize-space(),'Name (A to Z)')]")
    sort_name_za_locator = (By.XPATH, "//option[contains(normalize-space(),'Name (Z to A)')]")
    sort_price_lh_locator = (By.XPATH, "//option[contains(normalize-space(),'Price (low to high)')]")
    sort_price_hl_locator = (By.XPATH, "//option[contains(normalize-space(),'Price (high to low)')]")
    products_name_locator = (By.XPATH, "//div[@class='inventory_item_name']")
    products_price_locator = (By.XPATH, "//div[@class='inventory_item_price']")

    # End: Inventory page locators

    def add_a_product_to_cart(self, product_name, product_page):
        """
        Implementing add a product to cart functionality
        :param product_name, boolen product_page:
        :return:
        """
        # Temp variable for storing and updating varying locators.
        temp_product_item_locator = self.product_item_locator
        temp_product_add_button_locator = self.product_add_button_locator
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
            temp_product_add_button_locator = (
                temp_product_add_button_locator[0], temp_product_add_button_locator[1].format(product_name))

            # Click on the button using the updated locator
            self.click(temp_product_add_button_locator,
                       'Product add button locator not found before specified time out')

    def add_all_products_to_cart(self):
        """
        Implementing set password functionality
        :return:
        """
        product_names = self.find_elements(self.products_name_locator)
        product_values = [element.text for element in product_names]

        # Iterate through each product and add it to the cart
        for product_name in product_values:
            self.add_a_product_to_cart(product_name, False)

    def remove_a_product_to_cart(self, product_name, product_page):
        """
        Implementing remove the product from cart functionality
        :param product_name, boolean product_page:
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

    def sort(self, sort_criteria):
        """
        Implementing generic sorting functionality based on the specified criteria
        :param sort_criteria
        :return: is_sorted
        """
        sort_locator = None
        #  Determine the sort locator and element locator based on the sorting criteria.
        if sort_criteria == "Name A to Z":
            sort_locator = self.sort_name_az_locator
            element_locator = self.products_name_locator
        elif sort_criteria == "Name Z to A":
            sort_locator = self.sort_name_za_locator
            element_locator = self.products_name_locator
        elif sort_criteria == "Price Low to High":
            sort_locator = self.sort_price_lh_locator
            element_locator = self.products_price_locator
        elif sort_criteria == "Price High to Low":
            sort_locator = self.sort_price_hl_locator
            element_locator = self.products_price_locator

        # Click on the sort locator
        self.click(sort_locator, 'Sort Name locator not found before specified time out')

        # Get the list of element values based on the element locator
        element_elements = self.find_elements(element_locator)
        element_values = [element.text for element in element_elements]

        # Sort the element values based on the sorting criteria
        if sort_criteria in ["Name A to Z", "Price Low to High"]:
            sorted_values = sorted(element_values)
        elif sort_criteria in ["Name Z to A", "Price High to Low"]:
            sorted_values = sorted(element_values, reverse=True)

        # Check if the element values are sorted correctly
        is_sorted = element_values == sorted_values
