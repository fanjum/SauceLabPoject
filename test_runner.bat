cd "%~dp0"
@ECHO ON
SET TEST_SUITE="./RobotFramework/TestSuites
SET REPORT_PATH="./ExecutionReport"

CALL robot D:\RobotAutomation\TestProjects\SauceLabPoject\RobotFramework\TestSuites\TC_001_Log_in.robot
::CALL robot D:\RobotAutomation\TestProjects\SauceLabPoject\RobotFramework\TestSuites\TC_002_Product_Page_Navigation.robot
::CALL robot D:\RobotAutomation\TestProjects\SauceLabPoject\RobotFramework\TestSuites\TC_003_Add_Products_and_Checkout.robot
::CALL robot D:\RobotAutomation\TestProjects\SauceLabPoject\RobotFramework\TestSuites\TC_004_Add_A_Product_and_Checkout.robot

::CALL robot  -d %REPORT_PATH% -T -r REPORT -l LOG -o OUTPUT %TEST_SUITE%