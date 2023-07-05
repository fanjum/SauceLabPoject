"""Implements Test Startup settings"""

# import Modules.browser as Browser
import TestFramework.Modules.browser as browser
#from TestFramework.Modules import browser


class TestFixture:
    """
    Set of objects used as a baseline for running tests.
    Navigating to System Under Test
    Closing browser instance
    """

    def setup(self, browser_name):
        if (browser_name.lower() == 'chrome'):
            browser.open_chrome()
        else:
            browser.open_ie()

    def goto(self, value):
        """Launching/Navigating System Under Test"""
        browser.goto(value)

    def teardown(self):
        """Closing browser instance"""
        browser.quit()

    def capture_screenshot(self, directory):
        """
        Implementing capture screenshot functionality
        :param directory:
        :return: image path
        """
        return browser.capture_screenshot(directory)
