# Lab 7 Submission Notes

## Issues addressed in the assigned implementation

| Function | Input-validation weakness | Fix |
|---|---|---|
| `withdraw` | Non-integer values could cause TypeError or allow non-integer money values. | Validate integer types and reject booleans; check non-negative balance. |
| `withdraw` | Unhashable or non-string account types could raise an uncontrolled TypeError. | Validate the account type before dictionary lookup. |
| `withdraw` | `own_bank` accepted arbitrary truthy/falsy values. | Require a Boolean flag. |
| `pin_check` | Negative and non-integer attempt counts were accepted or caused unexpected comparisons. | Validate integer inputs and reject negative values. |
| `note_breakup` | Negative multiples of 100 produced negative note counts. | Reject negative amounts and invalid types. |
| all | Input contracts were implicit and inconsistent. | Use a shared integer validator that raises ValueError consistently. |

## Behaviour retained

- Savings daily limit: 25,000.
- Current daily limit: 50,000.
- Other-bank fee: 20; add 10 when withdrawal amount is over 10,000.
- PIN is blocked at 3 or more prior attempts; a wrong PIN at attempt count 2 blocks the card.
- Note breakup uses 500, 200, and 100 denominations.

## Verification status

The current ChatGPT execution environment did not have Hypothesis installed and could not reach the package index. The Hypothesis test file and Windows runner are prepared, but you must run them locally after installing requirements and capture the real terminal output. Do not claim a passing Hypothesis run until `python -m pytest -v test_atm_withdrawal.py` completes successfully.

## Evidence checklist

- [ ] Screenshot: initial application run
- [ ] Screenshot: failing fuzz tests on original version
- [ ] Screenshot: fixed application run
- [ ] Screenshot: passing fuzz tests on fixed version
- [ ] PDF containing the four genuine screenshots
