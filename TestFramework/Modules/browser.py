"""

Controls a browser by sending commands to a remote server.
Dictionary of effective capabilities of this browser session as returned by the remote server.
WebDriver Wait implementation
"""

import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller


from selenium.webdriver.chrome.service import Service

_driver = None
_screenshot_count = 0


@property
def driver():

    global _driver
    return _driver


def open_chrome():
    """
    Implementing launch Chrome browser functionality
    Create a new Chrome Driver instance by a dictionary of capabilities to request when
             starting the browser session.
    :return: driver instance
    """
    # global _driver
    # global _current_browser
    #
    # _current_browser = 'chrome'
    # caps = DesiredCapabilities.CHROME
    # caps['javascriptEnabled'] = True
    # caps['acceptSslCerts'] = True
    #
    # options = Options()
    # options.add_argument("--disable-extensions")
    # _driver = webdriver.Chrome()
    global _driver
    global _current_browser

    _current_browser = 'chrome'
    chrome_driver_path = chromedriver_autoinstaller.install()

    caps = DesiredCapabilities.CHROME
    caps['javascriptEnabled'] = True
    caps['acceptSslCerts'] = True

    options = Options()
    options.add_argument("--disable-extensions")

    options.add_experimental_option('prefs', {

        "download.prompt_for_download": False,  # To auto download the file
        "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
    })
    # options.add_experimental_option("excludeSwitches", ["enable-logging", 'enable-automation'])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    _driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=options, executable_path=chrome_driver_path)



def open_ie():
    """
    Implementing launch IE browser functionality
    Create a new Internext Explorer Driver instance by a dictionary of capabilities to request when
             starting the browser session.
    :return: driver instance
    """
    global _driver
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps['ignoreProtectedModeSettings'] = True
    caps['ignoreZoomSetting'] = True
    caps['initialBrowserUrl'] = ""
    caps['ensureCleanSession'] = True  # Cleanup session in IE Browser
    caps['enableElementCacheCleanup'] = True  # Clear WebElement Cache from IE
    # caps['requireWindowFocus'] = True
    _driver = webdriver.Ie(capabilities=caps)


def goto(value):
    """
    Implementing load web page functionality
    Loads a web page in the current browser session.
    :param value: URL
    :return:
    """
    global _driver
    maximize_window()
    delete_cookies()
    _driver.get(value)


def wait(value):
    """
    Implementing web driver wait functionality
    WebDriver Wait instance
    :param value: Seconds
    :return:
    """
    global _driver
    return WebDriverWait(_driver, value)


def maximize_window():
    """
    Implementing maximize browser window functionality
    Maximizes the current window that webdriver is using
    """
    global _driver
    _driver.maximize_window()


def delete_cookies():
    """
    Delete all cookies of browser
    Implementing delete cookies functionality
    """
    global _driver
    _driver.delete_all_cookies()
    _driver.refresh()


def close_browser():
    """
    Implementing close current window functionality
    Closes the current window.
    :return:
    """
    global _driver
    _driver.close()


def quit():
    """
    Implementing close browser functionality
    Quits the driver and closes every associated window.
    :return:
    """
    global _driver
    _driver.quit()


def capture_screenshot(directory):
    """
    Implementing capture screenshot functionality
    :return: image path
    """
    global _screenshot_count

    file_name = "screenshot_" + str.replace(str.replace(str(datetime.datetime.now()), ' ', '_'), ':', '') + "_" + str(
        _screenshot_count) + ".png"
    file_path = directory + "\\" + file_name
    _driver.get_screenshot_as_file(file_path)
    _screenshot_count += 1
    return file_name


def script_executor_click(element):
    global _driver
    _driver.execute_script("var elem=arguments[0]; setTimeout(function() {elem.click();}, 50)", element)


def find_elements(element):
    """Implementating finding element list by locator
    :return element list
    """
    global _driver
    return _driver.find_elements(*element)
