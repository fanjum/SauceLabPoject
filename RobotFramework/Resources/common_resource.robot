*** Settings ***
Documentation    A common resource file with reusable keywords and variables
Library    ../../TestFramework/TestFixture.py



*** Variables ***
${BROWSER NAME}                 chrome                                                      # Browser name.
${APP URL}                      https://www.saucedemo.com/                                  # Application URL.
${VALID USERNAME}               standard_user                                               # Valid User Name.
${VALID PASSWORD}               secret_sauce                                                # Valid Password.
${INVALID PASSWORD}             test1234                                                    # Invalid Password.
${LOCKEDOUT USERNAME}           locked_out_user                                             # Lockedout User Name.


*** Keywords ***
Validate Setup
    setup    ${BROWSER NAME}
    goto     ${APP URL}

Validate Teardown
    teardown

Log Screenshot
    ${SCREENSHOT DIRECTORY} =   get variable value      ${OUTPUT DIR}
    ${IMAGE PATH} =    capture screenshot     ${SCREENSHOT DIRECTORY}
    Log    <img src="${IMAGE PATH}">    HTML