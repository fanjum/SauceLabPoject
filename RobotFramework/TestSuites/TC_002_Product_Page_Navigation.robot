*** Settings ***
Documentation    Set of tests to test the navigation of the inventory page.

Resource        ../Resources/common_resource.robot
Resource        ../Resources/Pages/login_page_resource.robot
Resource        ../Resources/Pages/inventory_page_resource.robot
Resource        ../Resources/ExternalTestDataSource/add_product_test_data_source.robot

Suite Setup         Validate Setup
Suite Teardown      Validate Teardown
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

Sort products by Name A to Z
    [Documentation]  Sorting products by Name A to Z
    Verify sorting products        Name A to Z

Sort products by Name Z to A
    [Documentation]  Sorting products by Name Z to A
    Verify sorting products        Name Z to A

Sort products by Price Low to High
    [Documentation]  Sorting products by Price Low to High
    Verify sorting products        Price Low to High

Sort products by Price High to Low
    [Documentation]  Sorting products by High to Low
    Verify sorting products        Price High to Low

Click on a product then add to cart
    [Documentation]    Clicking on a product then adding the product to cart
    Verify adding a product to cart        ${PRODUCT NAME}      ${true}

Remove the product from the product page
    [Documentation]    Removing the added product from cart from the product page
    Verify removing a product to cart        ${PRODUCT NAME}      ${true}
