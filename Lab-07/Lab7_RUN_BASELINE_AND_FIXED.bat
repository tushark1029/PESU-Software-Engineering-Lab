@echo off
setlocal
cd /d "%~dp0"

python -m venv .venv
call .venv\Scripts\activate
python -m pip install -r requirements.txt
if errorlevel 1 goto :error

if not exist evidence mkdir evidence

echo ===== ORIGINAL APPLICATION DEMO =====
cd original
python -c "from atm_withdrawal import withdraw, pin_check, note_breakup; print('Original ATM module'); print('Withdrawal:', withdraw(20000, 5000, 'savings', True)); print('PIN:', pin_check(1234, 1234, 0)); print('Notes:', note_breakup(1200))" > ..\evidence\01_original_application.txt 2>&1

echo ===== EXPECTED FUZZ TEST FAILURES ON ORIGINAL =====
python -m pytest -v test_atm_withdrawal.py > ..\evidence\02_original_fuzz_failures.txt 2>&1
if errorlevel 1 (
  echo Original version exposed input-validation failures as expected.
) else (
  echo WARNING: Original tests did not fail; inspect the report.
)

cd ..
echo ===== FIXED APPLICATION =====
python atm_withdrawal.py > evidence\03_fixed_application.txt 2>&1
if errorlevel 1 goto :error

echo ===== FUZZ TESTS ON FIXED APPLICATION =====
python -m pytest -v test_atm_withdrawal.py > evidence\04_fixed_fuzz_tests.txt 2>&1
if errorlevel 1 goto :error

echo.
echo Completed. Open the four text files in evidence\ and capture genuine screenshots.
echo Put the screenshots into a PDF named Lab7_Fuzz_Testing_Evidence.pdf.
pause
exit /b 0

:error
echo A step failed. Review the output above or evidence files before continuing.
pause
exit /b 1
