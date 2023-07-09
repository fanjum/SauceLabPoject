*** Settings ***
Documentation    Set of test for testing log in functionality

Resource        ../Resources/common_resource.robot
Resource        ../Resources/Pages/login_page_resource.robot

Suite Teardown      Validate Teardown

*** Test Cases ***
Validate Successful Login
    [Documentation]  Login Functionality with valid set of credentials
    Validate Setup
    Verify Set User Name        ${VALID USERNAME}
    Verify Set Password         ${VALID PASSWORD}
    Verify Click Login Button

Validate Successful Logout
    [Documentation]  Logout Functionality
    Verify Menu Navigation
    Verify Successful Logout

Validate Unsuccessful Login
    [Documentation]  Login Functionality with invalid set of credentials
    Validate Setup
    Verify Set User Name        ${VALID USERNAME}
    Verify Set Password         ${INVALID PASSWORD}
    Verify Click Login Button




Validate Lockedout User Login
    [Documentation]  Login Functionality with valid set of credentials but user is lockedout
    Validate Setup
    Verify Set User Name        ${LOCKEDOUT USERNAME}
    Verify Set Password         ${VALID PASSWORD}
    Verify Click Login Button