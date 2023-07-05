"""
Implementing default run
"""
#import robot
from RobotFramework.Resources.TestFixture import TestFixture
#from TestFramework.Tests.Login import Login

if __name__ == "__main__":
    import time

    # print str(time.time()).replace('.', '-')
    #
    # # Open browser
    test = TestFixture()
    test.setup("chrome")
     #test_fixture.goto("https://www.saucedemo.com/")
    #
    #
    #login_page = Login()
    # login_page.set_user_name("standard_user")
    # login_page.set_password("secret_sauce")
    #
    # login_page.click_login_button()
    #robot.run("D:\Robot Automation\Test Projects\SauceLabPoject\RobotFramework\TestSuites\TC_001_Log_in.robot")
    # robot.run("D:\Robot Automation\Test Projects\SauceLabPoject\RobotFramework\TestSuites\TC_002_Add_Products_and_Checkout.robot")
