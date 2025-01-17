*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database

*** Test Cases ***
When article form is selected article form is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  acm
    Page Should Contain  Creating ACM type reference

When ACM Is Submitted Page Should Redirect To Main
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  acm
    Page Should Contain  Creating ACM type reference
    Set Name  ACMTest1
    Set Link   https://dl.acm.org/doi/10.1145/3695770
    Scroll Element Into View  acm_submit
    Click ACM Submit
    Main Page Should Be Open


*** Keywords ***
Set Name
    [Arguments]  ${name}
    Input Text  xpath=//form[@id='acm']//input[@name='name']  ${name}

Set Link
    [Arguments]  ${link}
    Input Text  xpath=//form[@id='acm']//input[@name='link']  ${link}

Click ACM Submit
    Click Button  acm_submit
