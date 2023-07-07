*** Settings ***
Documentation   Add to cart and checkout page resource with necessary keywords.

Resource        ../common_resource.robot
Library       ../../../TestFramework/Tests/Inventory.py


*** Variables ***
${STATUS}       False

*** Keywords ***
Verify adding a product to cart
    [Arguments]    ${PRODUCT}       ${PAGE}
    [Documentation]     Add a products to cart.
    ${STATUS} =     add a product to cart       ${PRODUCT}      ${PAGE}
    should be true    ${STATUS}     Unable to add product to cart
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

Verify removing a product to cart
    [Arguments]    ${PRODUCT}       ${PAGE}
    [Documentation]     Remove a products to cart.
    ${STATUS} =     remove a product to cart       ${PRODUCT}      ${PAGE}
    should be true    ${STATUS}     Unable to remove the product from cart
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

Verify sorting products
    [Arguments]    ${SORT CRITERIA}
    [Documentation]  Sort products according to the given criteria
    ${STATUS} =     sort       ${SORT CRITERIA}
    should be true    ${STATUS}     Unable to sort products
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

Verify adding all products to cart
    [Documentation]  Add all available products to cart
    ${STATUS} =     add all products to cart
    should be true    ${STATUS}     Unable to add all products
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot



#Verify Set Password
#    [Arguments]    ${PASSWORD}
#    [Documentation]     Set password into password input field. Take password as parameter.
#    ${STATUS} =    set password      ${PASSWORD}
#    should be true    ${STATUS}
#    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot


