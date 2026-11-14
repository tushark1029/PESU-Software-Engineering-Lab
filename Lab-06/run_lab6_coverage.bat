@echo off
setlocal
cd /d "%~dp0"

py -m pip install -r requirements.txt
if errorlevel 1 exit /b 1

echo.
echo ===== CODE COVERAGE =====
py -m coverage erase
py -m coverage run --source=atm_withdrawal -m pytest -q CodeCoverageTest_18_atm_withdrawal.py
if errorlevel 1 exit /b 1
py -m coverage report -m > Code_Coverage_Report.txt
type Code_Coverage_Report.txt

echo.
echo ===== BRANCH COVERAGE =====
py -m coverage erase
py -m coverage run --branch --source=atm_withdrawal -m pytest -q BranchCoverageTest_18_atm_withdrawal.py
if errorlevel 1 exit /b 1
py -m coverage report -m > Branch_Coverage_Report.txt
type Branch_Coverage_Report.txt

echo.
echo Done. Capture terminal screenshots of both successful results for submission.
pause
