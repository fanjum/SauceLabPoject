*** Settings ***
Documentation    Set of tests to Add Products and Checkout

Resource        ../Resources/common_resource.robot
Resource        ../Resources/Pages/login_page_resource.robot
Resource        ../Resources/Pages/inventory_page_resource.robot
Resource        ../Resources/ExternalTestDataSource/add_product_test_data_source.robot
Resource        ../Resources/Pages/cart_page_resource.robot

Suite Setup         Validate Setup
Suite Teardown      Validate Teardown

*** Test Cases ***
Validate Login
    [Documentation]  Login Functionality with valid set of credentials
    Verify Set User Name        ${VALID USERNAME}
    Verify Set Password         ${VALID PASSWORD}
    Verify Click Login Button

Add Products to Cart
    [Documentation]    Adding all available products to cart
    Verify adding all products to cart

Validate Cart items
    [Documentation]    Navigation to the cart and verifying the items selected
    Verify navigation to cart
    Verify the number of item selected

Validate Checkout
    [Documentation]    Checkout with the added products in cart
    Verify Click Checkout Button

Validate Checkout:Your Information
    Verify Set First Name        ${FIRST NAME}
    Verify Set Last Name         ${LAST NAME}
    Verify Set ZIP               ${ZIP}
    Verify Click Continue Button

Validate Checkout:Overview
    [Documentation]    Checkout with the added products in cart
    Verify Click Finish Button
    Verify Confirmation Message     ${SUCCESS MESSAGE}