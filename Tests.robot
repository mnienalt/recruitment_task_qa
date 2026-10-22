*** Settings ***
Library           StockLib.py


*** Test Cases ***
Validate If Sum Of Values For Target Percentage Column Is Equal 100
    [Documentation]
    [Tags]  TEST_ID=1

    Sum Of Values For Target Percentage Column Should Equal  100

Validate If Sum Of Values For Current Percentage Column Is Equal 100
    [Documentation]
    [Tags]  TEST_ID=2

    Sum Of Values For Current Percentage Column Should Equal  100

Validate If Target Variance Is Calculated Based On Target And Current
    [Documentation]
    [Tags]  TEST_ID=3

    Target Variance Is Calculated Correctly

Validate If Target Percent Is Always A Number From <0;100>
    [Documentation]
    [Tags]  TEST_ID=4

    Target Percent Between 0 And 100

Validate If Current Percent Is Always A Number From <0;100>
    [Documentation]
    [Tags]  TEST_ID=5

    Current Percent Between 0 And 100

Validate If Calculated Output Number Of Shares To Buy Or Sell Is Correct
    [Documentation]
    [Tags]  TEST_ID=6

    Calculated Output Number Of Shares Is Correct

Simulate That Calculated Output Number Of Shares To Buy Or Sell Is Incorrect
    [Documentation]
    [Tags]  TEST_ID=7

    Run Keyword And Expect Error  *  Simulate Output Number Of Shares Is Incorrect