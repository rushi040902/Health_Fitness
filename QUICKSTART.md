# Quick Start Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- MySQL Server (8.0 or higher)

## Installation Steps

### Windows Users:

1. **Open PowerShell or Command Prompt** in the project directory

2. **Run the setup script:**
   ```bash
   setup.bat
   ```
   This will:
   - Create a virtual environment
   - Install Django
   - Run database migrations
   - Populate sample food data
   - Optionally create a superuser

3. **Or manually:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py populate_foods
   ```

### Linux/Mac Users:

1. **Open Terminal** in the project directory

2. **Make setup script executable and run:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Or manually:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py populate_foods
   ```

## Running the Application

### Windows:
```bash
venv\Scripts\activate
python manage.py runserver
```

### Linux/Mac:
```bash
source venv/bin/activate
python manage.py runserver
```

Then open your browser and navigate to: **http://127.0.0.1:8000**

## First Steps

1. **Register a new account** or **login** if you already have one
2. **Set your calorie goal** by clicking "Edit Goal" button
3. **Start adding foods** from the dropdown
4. **Track your progress** with the progress bar and charts

## Adding More Foods

You can add more foods through:
- **Django Admin Panel**: http://127.0.0.1:8000/admin (requires superuser account)
- **Command line**: Run `python manage.py populate_foods` again (won't duplicate existing foods)

## Troubleshooting

**Issue: "No module named 'django'"**
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt`

**Issue: "Table doesn't exist"**
- Run `python manage.py migrate`

**Issue: "No foods available"**
- Run `python manage.py populate_foods`

**Issue: Static files not loading**
- Make sure `DEBUG = True` in settings.py (for development)
- Check that STATIC_URL and STATICFILES_DIRS are correctly set

## Admin Access

To access Django admin panel:
1. Create superuser: `python manage.py createsuperuser`
2. Visit: http://127.0.0.1:8000/admin
3. Login with superuser credentials

## Need Help?

Check the full README.md for detailed documentation and feature list.

