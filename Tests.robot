*** Settings ***
Library           StockLib.py


*** Test Cases ***
Validate If Sum Of Values For Target Percentage Column Is Equal 100
    [Documentation]  The purpose of this test is to verify if sum of target percentage column from csv file
    ...  is equal 100
    [Tags]  TEST_ID=1

    Sum Of Values For Target Percentage Column Should Equal  100

Validate If Sum Of Values For Current Percentage Column Is Equal 100
    [Documentation]  The purpose of this test is to verify if sum of current percentage column from csv file
    ...  is equal 100
    [Tags]  TEST_ID=2

    Sum Of Values For Current Percentage Column Should Equal  100

Validate If Target Variance Is Calculated Based On Target And Current
    [Documentation]  The purpose of this test is to verify if target variance is calculated correctly
    [Tags]  TEST_ID=3

    Target Variance Is Calculated Correctly

Validate If Target Percent Is Always A NUmber From <0;100>
    [Documentation]
    [Tags]  TEST_ID=3

    Target Percent Between 0 And 100

Validate If Current Percent Is Always A NUmber From <0;100>
    [Documentation]
    [Tags]  TEST_ID=3

    Current Percent Between 0 And 100