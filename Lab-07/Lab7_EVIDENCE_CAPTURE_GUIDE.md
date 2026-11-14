# Lab 7 - Evidence Capture Guide

The handout asks for a PDF containing screenshots of the original run, the failing fuzz tests, the fixed application run, and the passing fuzz tests.

## 1. Install dependencies

```powershell
cd path\to\Lab-07
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## 2. Capture the original/failing run

Open a new Command Prompt or PowerShell window:

```powershell
cd path\to\Lab-07\original
python atm_withdrawal.py
python -m pytest -v test_atm_withdrawal.py
```

The original module has no `main()` demo, so running it directly may produce no output. The pytest command should expose the missing input validation. Capture the pytest failure screen with `Win + Shift + S`.

## 3. Capture the fixed/passing run

```powershell
cd path\to\Lab-07
python atm_withdrawal.py
python -m pytest -v test_atm_withdrawal.py
```

Capture the output showing the application demo and all tests passing.

## 4. Make the PDF

Paste the genuine screenshots into Word in this order:
1. Original application run.
2. Fuzz test failures against the original version.
3. Fixed application run.
4. Fuzz tests passing against the fixed version.

Add a short caption under each screenshot. Save as `Lab7_Fuzz_Testing_Evidence.pdf`.

**Important:** Do not fabricate or edit terminal results. The Hypothesis tests must be run on your computer after installing the dependencies.
