# Lab 7 - Fuzzing for Input Validation Bugs

**Student:** Tushar Vibhakar Kulkarni  
**SRN:** PES2UG24AM174  
**Assigned assignment:** 18 - ATM Withdrawal  
**Assigned source repository:** https://github.com/SETAPESU26/L6_L7_18_atm_withdrawal

## Files

- `atm_withdrawal.py` - hardened application module.
- `test_atm_withdrawal.py` - Hypothesis property-based fuzz tests for all three functions.
- `original/atm_withdrawal.py` - original assigned implementation, retained for comparison.
- `requirements.txt` - Hypothesis and pytest dependencies.
- `run_lab7.bat` - Windows setup and test runner.
- `SUBMISSION_NOTES.md` - issues identified, fixes, and evidence checklist.

## Run on Windows

Open Command Prompt in this folder and run:

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python atm_withdrawal.py
python -m pytest -v test_atm_withdrawal.py
```

The handout uses generic names `processor.py` and `test_processor.py`; the assigned repository's Lab 7 folder uses `atm_withdrawal.py` and `test_atm_withdrawal.py`, so this submission preserves the assigned filenames.

## Required evidence

Capture genuine terminal screenshots from your computer showing:
1. Initial application output.
2. Fuzz test failures against the original application (before fixes).
3. Fixed application output.
4. All Hypothesis tests passing against the fixed application.

Put the screenshots in `evidence/` and combine them into the required PDF before submission. Do not use placeholder or recreated screenshots.

For original-vs-fixed comparison, run `RUN_BASELINE_AND_FIXED.bat`. It saves terminal outputs as text files under `evidence/`; capture genuine screenshots from those outputs and create the PDF requested by the handout.
