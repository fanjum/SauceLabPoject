"""Base Page implementations"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import TestFramework.Modules.browser as Browser


class BasePage:
    """
    Contain global level page implementations
    Class level variables
    Wait function
    Maximize window function
    Minimize window function
    Select item from dropdown functionality
    Click element functionality
    Select checkbox function
    Set value into text field
    """

    def wait(self, value=60):
        """
        Implementing wait functionality
        :param value: Seconds
        :return:WebDriver Wait instance
        """
        return Browser.wait(value)

    def maximize_window(self):
        """
        Implementing maximize window functionality
        Maximizes the current window that webdriver is using
        :return: Window Maximize
        """
        Browser.maximize_window()

    def close_browser(self):
        """
        Implementing close browser functionality
        :return: Closes the current window.
        """
        Browser.close_browser()

    def quit_browser(self):
        """
        Implementing quit browser functionality
        :return: Quit browser.
        """
        Browser.quit()

    def set_value_into_intput_field(self, locator, value, error_message=None, input_field_label=None):
        """
        Implementing set value into input field functionality
        :param locator:
        :param value:
        :param error_message:
        :param input_field_label:
        :return:
        """
        if input_field_label is not None:
            input_field_locator = (
            By.XPATH, "//td[contains(text(), '%s')]/following-sibling::td/input[@class='input']" % (input_field_label))
            element = self.wait().until(EC.presence_of_element_located(input_field_locator),
                                        'input field locator not found before specified time out')
        else:
            element = self.wait().until(EC.presence_of_element_located(locator), error_message)
        element.click()
        element.clear()
        element.send_keys(value)

    def click(self, locator, error_message, script_executor=False):
        """
        Implementing click element functionality
        :param locator:
        :param error_message:
        :return:
        """
        element = self.wait().until(EC.element_to_be_clickable(locator), error_message)
        if script_executor:
            Browser.script_executor_click(element)
        else:
            element.click()

    def select_item_from_dropdown(self, dropdown_label, dropdown_item):
        """
        Implementing select item from dropdown functionality
        :param dropdown_label:
        :param dropdown_item:
        :return:
        """
        dropdown_locator = (By.XPATH, "//td[text()='%s']/../descendant::select" % (dropdown_label))
        dropdown_element = self.wait().until(EC.presence_of_element_located(dropdown_locator))
        select_tag_locator = (By.XPATH, "//select[@id='%s']" % dropdown_element.get_attribute('id'))
        all_items = Select(self.wait().until(EC.presence_of_element_located(select_tag_locator)))
        all_items.select_by_visible_text(dropdown_item)

    def select_checkbox(self, checkbox_label):
        """
        Implementing select checkbox functionality
        :param checkbox_label:
        :return:
        """
        checkbox_locator = (By.XPATH, "//label[text()='%s']/../input[@type='checkbox']" % (checkbox_label))
        self.click(locator=checkbox_locator, error_message='checkbox locator not found before specified time out')

    def find_elements(self, elements_locator):
        """
        Implementing finding all elements based on the provided locator functionality.
        :param elements_locator:
        :return:
        """
        return Browser.find_elements(elements_locator)
