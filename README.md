# Health & Fitness Calorie Tracker

A Django-based web application for tracking calories and nutritional intake. Users can log meals, track daily calorie consumption, set calorie goals, and visualize their nutrient breakdown with interactive charts.

## Features

- **Food Logging**: Add foods to your daily consumption with quantity tracking
- **Calorie Goal Tracking**: Set and monitor daily calorie goals with progress bars
- **Nutritional Analysis**: Track carbs, protein, fats, and calories
- **Data Visualization**: Interactive pie/donut charts showing nutrient breakdown using Chart.js
- **User Authentication**: Secure user registration and login system
- **Today's Summary**: View all consumed foods with totals for the day

## Installation

1. **Clone or navigate to the project directory**

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
```

3. **Activate the virtual environment**:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

5. **Run migrations**:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser** (optional, for admin access):
```bash
python manage.py createsuperuser
```

7. **Populate sample food data**:
```bash
python manage.py populate_foods
```

8. **Run the development server**:
```bash
python manage.py runserver
```

9. **Access the application**:
   - Open your browser and navigate to: `http://127.0.0.1:8000`
   - Register a new account or login
   - Start tracking your calories!

## Usage

1. **Register/Login**: Create an account or login to access your personal calorie tracker
2. **Set Calorie Goal**: Click "Edit Goal" to set your daily calorie target (default: 2000 Kcal)
3. **Add Foods**: Search and select foods from the dropdown, specify quantity, and click "Add"
4. **View Progress**: Monitor your calorie progress with the progress bar
5. **View Breakdown**: See your nutrient breakdown (carbs, protein, fats) in the interactive chart
6. **Remove Items**: Click the red "×" button to remove any food item from today's consumption

## Technology Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (default, easily configurable to PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, JavaScript
- **Charts**: Chart.js (CDN)
- **Authentication**: Django's built-in authentication system

## Project Structure

```
calorie_tracker/
├── calorie_tracker/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tracker/                  # Main app
│   ├── models.py            # Food, Consumption, UserProfile models
│   ├── views.py             # View functions
│   ├── urls.py              # URL routing
│   ├── admin.py             # Admin configuration
│   ├── templates/           # HTML templates
│   └── static/              # CSS and JavaScript files
├── manage.py
└── requirements.txt
```

## Models

- **Food**: Stores food items with nutritional information (carbs, protein, fats, calories)
- **UserProfile**: Extended user profile with calorie goal setting
- **Consumption**: Tracks user's daily food consumption

## Customization

- To add more foods, use the Django admin panel or run the `populate_foods` management command
- Modify `calorie_goal` default in `UserProfile` model to change the initial goal
- Customize colors and styling in `tracker/static/tracker/css/style.css`
- Integrate external APIs (Edamam, FatSecret) in views.py for real-time food data

## Future Enhancements

- Integration with external nutrition APIs (Edamam, FatSecret)
- Weekly and monthly progress tracking
- Food search with autocomplete
- Meal planning features
- Export data to CSV/PDF
- Integration with fitness wearables (Fitbit, Apple Health)

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

