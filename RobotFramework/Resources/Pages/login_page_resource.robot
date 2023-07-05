*** Settings ***
Documentation   Login Page Resource File With Necessary Keywords.

Resource        ../common_resource.robot
Library       ../../../TestFramework/Tests/Login.py


*** Variables ***
${STATUS}       False

*** Keywords ***
Verify Set User Name
    [Arguments]    ${USERNAME}
    [Documentation]     Set user name into user name input field. Take user name as parameter.
    ${STATUS} =     set user name       ${USERNAME}
    should be true    ${STATUS}
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

Verify Set Password
    [Arguments]    ${PASSWORD}
    [Documentation]     Set password into password input field. Take password as parameter.
    ${STATUS} =    set password      ${PASSWORD}
    should be true    ${STATUS}
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

Verify Click Login Button
    [Documentation]     click login button.
    ${STATUS} =     click login button
    should be true      ${STATUS}
    [Teardown]      run keyword if    '${STATUS}'=='False'          Log Screenshot
