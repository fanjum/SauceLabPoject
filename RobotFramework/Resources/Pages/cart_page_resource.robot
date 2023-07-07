*** Settings ***
Documentation   Cart page resource with necessary keywords.

Resource        ../common_resource.robot
Library       ../../../TestFramework/Tests/Inventory.py


*** Variables ***
${STATUS}       False

*** Keywords ***
Verify the number of item selected
    [Documentation]     Verifying the number of items selected in the cart at top right corner.
    ${STATUS} =     add a product to cart       ${PRODUCT}      ${PAGE}
    should be true    ${STATUS}     Unable to add product to cart
    [Teardown]      run keyword if      '${STATUS}'=='False'        Log Screenshot




