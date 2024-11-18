*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Information
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Information
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  ka
    Set Password Confirmation  ka
    Submit Information
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Submit Information
    Register Should Fail With Message  Password must contain at least one number or special character

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle1234
    Submit Information
    Register Should Fail With Message  Password confirmation and password should match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Information
    Register Should Succeed
    Log Out
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Information
    Register Should Fail With Message  Username is already in use

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Information
    Register Should Succeed
    Log Out
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle1234
    Submit Information
    Register Should Fail With Message  Password confirmation and password should match
    Log Out
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Succeed
    Welcome Page Should Be Open

Submit Information
    Click Button  Register

Submit Credentials
    Click Button  Login

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
