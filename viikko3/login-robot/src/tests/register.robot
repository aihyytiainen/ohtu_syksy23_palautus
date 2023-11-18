*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kekke  ruusi45

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle456
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ju  juupas33
    Output Should Contain  Username minimun length is 3 letters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle1  kalle123
    Output Should Contain  Username shall contain only letters from a to z

Register With Valid Username And Too Short Password
    Input Credentials  jooseppi  jes2
    Output Should Contain  Password minimun length is 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jooseppi  kleptomaani
    Output Should Contain  Password can not be only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
