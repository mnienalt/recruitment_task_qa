# Manual Test Cases - description

## Assumptions

- The account value is **$100,000**.
- The trade amount is calculated from the absolute target variance percentage.
- The recommended share count can be expressed as a number with decimal part
- For invalid input, the expected behavior is to reject the affected input and report the row and field that caused the error. The application should not silently produce a recommendation from invalid data.

## Test Cases

| ID | Test case | Input / scenario | Expected result |
|---|---|---|---|
| TC-01 | Underweight security | IBM: variance **−10%**, unit price **$150** | Buy $10,000 / $150 = **66.67 shares**; share recommendation: **66.67**. |
| TC-02 | Overweight security | ORCL: variance **+10%**, unit price **$220** | Sell $10,000 / $220 = **45.45 shares**; share recommendation: **45.45**. |
| TC-03 | Security at target | MSFT: variance **0%** | No shares to buy or sell; recommendation: **0**. |
| TC-04 | Multiple securities | Process the supplied portfolio CSV | Recommendations match the correct securities: **IBM 66.67, MSFT 0, ORCL 45.45, AAPL 0, HD 0**. |
| TC-09 | Zero unit price | A security has a unit price of **0**. | Reject the invalid input and report the affected row and `unit price` field. Do not produce a recommendation. |
| TC-10 | Negative unit price | A security has a negative unit price. | Reject the invalid input and report the affected row and `unit price` field. Do not produce a recommendation. |
| TC-11 | Missing unit price | A security's unit price is empty or missing. | Reject the invalid input and report the affected row and `unit price` field. Do not produce a recommendation. |
| TC-12 | Non-numeric unit price | A security's unit price contains text instead of a number. | Reject the invalid input and report the affected row and `unit price` field. Do not produce a recommendation. |
| TC-13 | Missing target variance | A security's target variance is empty or missing. | Reject the invalid input and report the affected row and `target variance [%]` field. Do not produce a recommendation. |
| TC-14 | Non-numeric target variance | A security's target variance contains text instead of a number. | Reject the invalid input and report the affected row and `target variance [%]` field. Do not produce a recommendation. |
| TC-15 | Check total percent of target column | Sum all values of `target [%]` column. The sum should be equal 100 | If condition is met - process csv file. If not -reject the invalid input and report the affected error. |
| TC-16 | Check total percent of current column | Sum all values of `current[%]` column. The sum should be equal 100 | If condition is met - process csv file. If not -reject the invalid input and report the affected error. |
| TC-17 | Check if target variance is a substraction of `current[%]` column and `target [%]`| For each position in the column target variance should be equal (`current[%]` - `target [%]`) | If condition is met - process csv file. If not -reject the invalid input and report the affected error. |


## Notes

- Invalid-input cases assume the application rejects the invalid row and reports a clear error. What need to be confirmed? Whether the actual business requirement is to reject only that row or the entire CSV file.
- For CSV-level checks, verify each recommendation is associated with the correct security, not just that the output quantities appear somewhere in the file.
