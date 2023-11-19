*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  kekke
    Set Password  ruusi1234
    Set Password Confirmation  ruusi1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  je
    Set Password  qwerty1
    Set Password Confirmation  qwerty1
    Submit Credentials
    Register Should Fail With Message  Username minimun length is 3 letters

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Go To Register Page
    Set Username  jeepio
    Set Password  jeepiopio
    Set Password Confirmation  jeepiopio
    Submit Credentials
    Register Should Fail With Message  Password can not be only letters

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  jeepio
    Set Password  jeepio123
    Set Password Confirmation  jeepio124
    Submit Credentials
    Register Should Fail With Message  Password and confirmation do not match

Login After Successful Registration
    Go To Register Page
    Set Username  kekkee
    Set Password  ruusi12345
    Set Password Confirmation  ruusi12345
    Submit Credentials
    Go To Login Page
    Set Username  kekkee
    Set Password  ruusi12345
    Submit Login
    Login Should Succeed


Login After Failed Registration
    Go To Register Page
    Set Username  jeepiooo
    Set Password  jeepiopio
    Set Password Confirmation  jeepiopio
    Submit Credentials
    Register Should Fail With Message  Password can not be only letters
    Go To Login Page
    Set Username  jeepiooo
    Set Password  jeepiopio
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

Register Should Succeed
    Page Should Contain  Welcome
