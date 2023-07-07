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




