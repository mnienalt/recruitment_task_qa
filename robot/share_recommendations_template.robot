*** Settings ***
Documentation     Share recommendation rounding and invalid-input cases.
Library           ${CURDIR}${/}ShareCalculationLibrary.py
Test Template     Share Recommendation Scenario

*** Test Cases ***    VARIANCE       UNIT-PRICE    EXPECTED-BUY    EXPECTED-SELL    EXPECTED-RECOMMENDATION    EXPECTED-ERROR
Buy trolo             -1            2000          0.5             0                0                           NONE
Buy 0.5 Shares        -1            2000          0.5             0                0                           NONE
Buy 1.5 Shares        -3            2000          1.5             0                2                           NONE
Sell 0.5 Shares       1             2000          0               0.5              0                           NONE
Sell 1.5 Shares       3             2000          0               1.5              2                           NONE
Zero Price            -10           0             -               -                -                           *
Negative Price        -10           -150          -               -                -                           *
Missing Price         -10           ${EMPTY}      -               -                -                           *
Non-Numeric Price     -10           not-a-number  -               -                -                           *
Missing Variance      ${EMPTY}      150           -               -                -                           *
Non-Numeric Variance  not-a-number  150           -               -                -                           *

*** Keywords ***
Share Recommendation Scenario
    [Arguments]    ${variance}    ${unit_price}    ${expected_buy}    ${expected_sell}
    ...    ${expected_recommendation}    ${expected_error}

    IF    $expected_error == "NONE"
        ${buy}=    Calculate Number Of Shares To Buy    ${variance}    ${unit_price}
        ${sell}=    Calculate Number Of Shares To Sell    ${variance}    ${unit_price}
        ${recommendation}=    Calc Output Number    ${buy}    ${sell}

        Should Be Equal As Numbers    ${buy}    ${expected_buy}    precision=8
        Should Be Equal As Numbers    ${sell}    ${expected_sell}    precision=8
        Should Be Equal As Integers    ${recommendation}    ${expected_recommendation}
    ELSE
        Run Keyword And Expect Error
        ...    ${expected_error}
        ...    Calculate Recommendation
        ...    ${variance}
        ...    ${unit_price}
    END

Calculate Recommendation
    [Arguments]    ${variance}    ${unit_price}
    ${buy}=    Calculate Number Of Shares To Buy    ${variance}    ${unit_price}
    ${sell}=    Calculate Number Of Shares To Sell    ${variance}    ${unit_price}
    ${recommendation}=    Calc Output Number    ${buy}    ${sell}
