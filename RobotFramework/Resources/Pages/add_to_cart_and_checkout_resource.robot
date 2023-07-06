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
    should be true    ${STATUS}
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

Verify removing a product to cart
    [Arguments]    ${PRODUCT}
    [Documentation]     Add a products to cart.
    ${STATUS} =     remove a product to cart       ${PRODUCT}
    should be true    ${STATUS}
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot

#Verify clicking and adding a product to cart
#    [Arguments]    ${PRODUCT}       ${PAGE}
#    [Documentation]     Clicking on a product and adding to cart.
#    ${STATUS} =     add a product to cart       ${PRODUCT}      ${PAGE}
#    should be true    ${STATUS}
#    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot





#Verify Set Password
#    [Arguments]    ${PASSWORD}
#    [Documentation]     Set password into password input field. Take password as parameter.
#    ${STATUS} =    set password      ${PASSWORD}
#    should be true    ${STATUS}
#    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot


