@echo off
echo Python Template Setup
echo ====================
echo.
echo This script will help you set up your Python project from the template.
echo You will need to specify an output directory for your new project.
echo.

if "%1"=="" (
    echo Usage: setup_template.bat --output-dir ^<project-directory^>
    echo Example: setup_template.bat --output-dir my-new-project
    echo.
    pause
    exit /b 1
)

python replace_template_vars.py %*

if %ERRORLEVEL% == 0 (
    echo.
    echo Setup complete! You can now:
    echo 1. Navigate to your project directory
    echo 2. Review the generated files
    echo 3. Initialize git: git init
    echo 4. Install dependencies: poetry install --with dev,lint,test,docs
    echo 5. Run tests: poetry run pytest
)

pause