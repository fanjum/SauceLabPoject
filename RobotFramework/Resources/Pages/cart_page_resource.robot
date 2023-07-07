*** Settings ***
Documentation   Cart page resource with necessary keywords.

Resource        ../common_resource.robot
Library       ../../../TestFramework/Tests/Inventory.py
Library       ../../../TestFramework/Tests/Cart.py


*** Variables ***
${STATUS}       False

*** Keywords ***
Verify navigation to cart
    [Documentation]     Verifying navigation to cart page.
    ${STATUS} =     click cart icon
    should be true    ${STATUS}     Unable to click cart icon
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

#Verify the number of item selected
#    [Documentation]     Verifying the number of items selected in the cart at top right corner.
#    ${STATUS} =     add a product to cart       ${PRODUCT}      ${PAGE}
#    should be true    ${STATUS}     Unable to add product to cart
#    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

Verify Click Checkout Button
    [Documentation]     Verifying clicking checkout button.
    ${STATUS} =     click checkout button
    should be true    ${STATUS}     Unable to click cart icon
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

Verify Set First Name
    [Arguments]    ${FIRST NAME}
    [Documentation]     Set first name into first name input field. Take first name as parameter.
    ${STATUS} =     set first name       ${FIRST NAME}
    should be true    ${STATUS}
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

Verify Set Last Name
    [Arguments]    ${LAST NAME}
    [Documentation]     Set last name into last name input field. Take last name as parameter.
    ${STATUS} =     set last name       ${LAST NAME}
    should be true    ${STATUS}
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

Verify Set ZIP
    [Arguments]    ${ZIP}
    [Documentation]     Set zip into zip/postal code input field. Take zip as parameter.
    ${STATUS} =     set zip       ${ZIP}
    should be true    ${STATUS}
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot


