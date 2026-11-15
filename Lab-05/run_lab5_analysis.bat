@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" py -3 -m venv .venv
if errorlevel 1 exit /b 1
call ".venv\Scripts\activate.bat"
python -m pip install -r requirements-dev.txt
if errorlevel 1 exit /b 1
python -m pylint supplier_orders.py
python -m bandit -r supplier_orders.py
python -m flake8 supplier_orders.py
python -m unittest -v test_supplier_orders.py
