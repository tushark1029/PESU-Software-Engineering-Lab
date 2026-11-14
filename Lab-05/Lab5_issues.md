# Lab 5 - Static Analysis Issue Register

**Project:** Supplier Purchase Order Tracker  
**Assigned repository:** [L5_18_supplier_orders](https://github.com/SETAPESU26/L5_18_supplier_orders)  
**Assigned source file:** `supplier_orders.py`  
**Student:** Tushar Vibhakar Kulkarni  
**SRN:** PES2UG24AM174

> Line numbers below refer to the original starter file in `original/supplier_orders.py`. The uploaded three-page handout does not include actual tool report output or explicit Pylint/Bandit/Flake8 diagnostic codes. Use `run_lab5_analysis.bat` to generate the genuine before-and-after reports on your computer; do not treat these code-review mappings as a substitute for those generated reports.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| SQL statement built with string interpolation | Security | 11 | Supplier and item text are inserted directly into SQL text. Crafted values could alter the SQL statement. | Use SQLite parameter placeholders (`?`) and pass values separately. |
| Shell command constructed from supplier data | Security | 21 | `os.system()` runs a shell command assembled by string concatenation. Shell metacharacters in the value could change the command. | Remove the shell call and use the Python logging module for the warehouse notification message. |
| Global mutable order counter | Code quality / maintainability | 6, 10, 12-13, 40 | `order_total` is shared module state and `placeOrder()` modifies it with `global`, making the function harder to test and reuse. | Store the cumulative quantity in the SQLite database and retrieve it when needed. |
| Broad exception is silently ignored | Reliability | 25-28 | `except Exception: pass` hides database errors, so cleanup failures are not visible. | Remove the blanket exception suppression; allow database errors to surface to the caller. |
| Unused `remarks` parameter | Code quality | 16-17 | `markReceived()` accepts a remarks value but does not store or use it. | Add a `remarks` column and save the supplied value with the receipt update. |
| Non-standard function naming and missing documentation | Maintainability | 9, 16, 20, 24, 31, 35 | CamelCase function names do not follow common Python naming conventions; the starter lacks module and function docstrings. | Rename functions to `snake_case` and add concise docstrings. |
| Spacing and long-line formatting problems | Style | 5, 11-12, 32 | The starter contains long statements and missing spaces around the `+=` operator. | Wrap SQL and expressions across lines and apply standard Python spacing. |

## Resolution summary

The cleaned `supplier_orders.py` uses parameterized SQL, avoids shell execution, stores order totals in the database instead of a global variable, persists receipt remarks, removes silent broad exception handling, uses `snake_case` names and includes docstrings. It also formats long statements across multiple lines.

## Verification to complete on the student computer

1. Run `run_lab5_analysis.bat` to create the six actual report files under `reports/before/` and `reports/after/`.
2. Confirm that Bandit reports no remaining findings in the cleaned file.
3. Confirm that Flake8 reports no style violations in the cleaned file.
4. Confirm that Pylint reports a score greater than 9.5 for the cleaned file. The actual score must be read from `reports/after/pylint_report.txt`.
