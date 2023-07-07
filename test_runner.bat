cd "%~dp0"
@ECHO ON
SET TEST_SUITE="./RobotFramework/TestSuites/TC_001_Log_in.robot"
SET REPORT_PATH="./ExecutionReport"

CALL robot D:\RobotAutomation\TestProjects\SauceLabPoject\RobotFramework\TestSuites\TC_002_Product_Page_Navigation.robot
::CALL robot  -d %REPORT_PATH% -T -r REPORT -l LOG -o OUTPUT %TEST_SUITE%