*** Settings ***
Documentation    Set of tests to Add Products and Checkout

Resource        ../Resources/common_resource.robot
Resource        ../Resources/Pages/login_page_resource.robot
Resource        ../Resources/Pages/add_to_cart_and_checkout_resource.robot
Resource        ../Resources/ExternalTestDataSource/add_product_test_data_source.robot

Suite Setup         Validate Setup
*** Test Cases ***
Validate Login
    [Documentation]  Login Functionality with valid set of credentials
    Verify Set User Name        ${VALID USERNAME}
    Verify Set Password         ${VALID PASSWORD}
    Verify Click Login Button

Add Products to Cart
    [Documentation]    Adding all available products to cart
    Verify adding all products to cart