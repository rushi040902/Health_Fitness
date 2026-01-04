#!/bin/bash

echo "Setting up Health & Fitness Calorie Tracker..."
echo

echo "Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error creating virtual environment"
    exit 1
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error installing dependencies"
    exit 1
fi

echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Creating superuser (optional - press Ctrl+C to skip)..."
python manage.py createsuperuser

echo "Populating sample food data..."
python manage.py populate_foods

echo
echo "Setup complete!"
echo
echo "To run the server, use:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo

