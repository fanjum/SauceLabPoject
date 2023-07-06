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
    [Documentation]    Adding available products to cart
    Verify adding a product to cart        ${PRODUCT NAME}      ${false}

Remove the product to cart
    [Documentation]    Removing the added product from cart
    Verify removing a product to cart        ${PRODUCT NAME}      ${false}

Click on a product then add to cart
    [Documentation]    Clicking on a product then adding the product to cart
    Verify adding a product to cart        ${PRODUCT NAME}      ${true}

Remove the product from the product page
    [Documentation]    Removing the added product from cart from the product page
    Verify removing a product to cart        ${PRODUCT NAME}      ${true}

