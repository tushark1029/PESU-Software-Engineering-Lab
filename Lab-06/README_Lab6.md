# Lab 6 — Code and Branch Coverage Analysis

**Student:** Tushar Vibhakar Kulkarni  
**SRN:** PES2UG24AM174  
**Assignment:** 18 — ATM Withdrawal  
**Assigned repository:** https://github.com/SETAPESU26/L6_L7_18_atm_withdrawal

## Application
`atm_withdrawal.py` is the assigned ATM withdrawal module. It validates account type and withdrawal amounts, enforces account-specific daily limits, applies other-bank fees, checks PIN attempts, and calculates note breakup. The application source is retained unchanged from the assigned Lab 6 repository.

## Test files
- `CodeCoverageTest_18_atm_withdrawal.py` — expanded tests for statement/code coverage.
- `BranchCoverageTest_18_atm_withdrawal.py` — tests designed to exercise both outcomes of decision branches.

## Results
| Stage | Initial starter tests | Expanded tests |
|---|---:|---:|
| Code/statement coverage | 41% | **100%** (34/34 statements) |
| Branch coverage | 38% | **100%** (22/22 branches; 0 partial) |

- Code-coverage suite: 8 tests passed.
- Branch-coverage suite: 7 tests passed.

See `reports/` for text reports and `screenshots/` for terminal-result captures. `reports/initial_baseline.txt` records the starting coverage from the original two tests.

## Run on Windows
Open Command Prompt or PowerShell in this folder and run:

```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py -m coverage run --source=atm_withdrawal -m pytest -q CodeCoverageTest_18_atm_withdrawal.py
py -m coverage report -m
py -m coverage erase
py -m coverage run --branch --source=atm_withdrawal -m pytest -q BranchCoverageTest_18_atm_withdrawal.py
py -m coverage report -m
```

Alternatively, run `run_lab6_coverage.bat`.

## Required commits
The handout requires at least two commits:
1. `Add Lab 6 code coverage tests and results` — code-coverage test and its result screenshot/report.
2. `Add Lab 6 branch coverage tests and results` — branch-coverage test and its result screenshot/report.
