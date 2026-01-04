@echo off
echo Setting up Health & Fitness Calorie Tracker...
echo.

echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Error creating virtual environment
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error installing dependencies
    pause
    exit /b 1
)

echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo Creating superuser (optional)...
echo You can skip this step by pressing Ctrl+C
python manage.py createsuperuser

echo Populating sample food data...
python manage.py populate_foods

echo.
echo Setup complete!
echo.
echo To run the server, use:
echo   venv\Scripts\activate
echo   python manage.py runserver
echo.
pause

