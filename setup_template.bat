@echo off
echo Python Template Setup
echo ====================
echo.
echo This script will help you set up your Python project from the template.
echo.

python replace_template_vars.py %*

if %ERRORLEVEL% == 0 (
    echo.
    echo Setup complete! You can now:
    echo 1. Review the generated files
    echo 2. Initialize git: git init
    echo 3. Install dependencies: poetry install --with dev,lint,test,docs
    echo 4. Run tests: poetry run pytest
)

pause