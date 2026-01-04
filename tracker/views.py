from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import date
import json

from .models import Food, Consumption, UserProfile


def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile with default calorie goal
            UserProfile.objects.create(user=user, calorie_goal=2000)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome {username}! Your account has been created successfully.')
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})


def login_view(request):
    """Custom login view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Please provide both username and password.')
    
    return render(request, 'tracker/login.html')


@login_required
def home(request):
    """Main calorie tracking page"""
    user = request.user
    
    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(
        user=user,
        defaults={'calorie_goal': 2000}
    )
    
    # Get today's consumption
    today = date.today()
    today_consumption = Consumption.objects.filter(
        user=user,
        date=today
    )
    
    # Calculate totals for today
    total_carbs = sum(c.total_carbs for c in today_consumption)
    total_protein = sum(c.total_protein for c in today_consumption)
    total_fats = sum(c.total_fats for c in today_consumption)
    total_calories = sum(c.total_calories for c in today_consumption)
    
    # Get all foods for the dropdown
    foods = Food.objects.all()
    
    # Calculate calorie progress
    calorie_progress = min((total_calories / profile.calorie_goal) * 100, 100) if profile.calorie_goal > 0 else 0
    
    context = {
        'profile': profile,
        'today_consumption': today_consumption,
        'foods': foods,
        'total_carbs': total_carbs,
        'total_protein': total_protein,
        'total_fats': total_fats,
        'total_calories': total_calories,
        'calorie_progress': calorie_progress,
    }
    
    return render(request, 'tracker/home.html', context)


@login_required
@require_POST
def add_food(request):
    """Add food to today's consumption"""
    try:
        data = json.loads(request.body)
        food_id = data.get('food_id')
        quantity = float(data.get('quantity', 1.0))
        
        food = get_object_or_404(Food, id=food_id)
        today = date.today()
        
        # Create new consumption entry
        Consumption.objects.create(
            user=request.user,
            food=food,
            date=today,
            quantity=quantity
        )
        
        return JsonResponse({
            'success': True,
            'message': f'{food.name} added successfully'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)


@login_required
@require_POST
def remove_food(request, consumption_id):
    """Remove food from consumption"""
    try:
        consumption = get_object_or_404(Consumption, id=consumption_id, user=request.user)
        consumption.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)


@login_required
@require_POST
def update_calorie_goal(request):
    """Update user's calorie goal"""
    try:
        data = json.loads(request.body)
        calorie_goal = int(data.get('calorie_goal', 2000))
        
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.calorie_goal = calorie_goal
        profile.save()
        
        return JsonResponse({'success': True, 'calorie_goal': calorie_goal})
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)


@login_required
def search_foods(request):
    """Search foods by name"""
    query = request.GET.get('q', '')
    foods = Food.objects.filter(name__icontains=query)[:10]
    food_list = [{
        'id': food.id,
        'name': food.name,
        'carbs': food.carbs,
        'protein': food.protein,
        'fats': food.fats,
        'calories': food.calories
    } for food in foods]
    return JsonResponse({'foods': food_list})


@staff_member_required
def admin_home(request):
    """Admin panel home"""
    return render(request, 'tracker/admin/base.html')


@staff_member_required
def food_list(request):
    """List all foods for admin"""
    foods = Food.objects.all()
    return render(request, 'tracker/admin/food_list.html', {'foods': foods})


@staff_member_required
def food_create(request):
    """Create new food"""
    if request.method == 'POST':
        name = request.POST.get('name')
        carbs = request.POST.get('carbs')
        protein = request.POST.get('protein')
        fats = request.POST.get('fats')
        calories = request.POST.get('calories')
        if name and carbs and protein and fats and calories:
            Food.objects.create(
                name=name,
                carbs=float(carbs),
                protein=float(protein),
                fats=float(fats),
                calories=float(calories)
            )
            messages.success(request, 'Food created successfully.')
            return redirect('food_list')
        else:
            messages.error(request, 'All fields are required.')
    return render(request, 'tracker/admin/food_form.html', {'action': 'Create'})


@staff_member_required
def food_update(request, food_id):
    """Update existing food"""
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        food.name = request.POST.get('name')
        food.carbs = float(request.POST.get('carbs'))
        food.protein = float(request.POST.get('protein'))
        food.fats = float(request.POST.get('fats'))
        food.calories = float(request.POST.get('calories'))
        food.save()
        messages.success(request, 'Food updated successfully.')
        return redirect('food_list')
    return render(request, 'tracker/admin/food_form.html', {'food': food, 'action': 'Update'})


@staff_member_required
def food_delete(request, food_id):
    """Delete food"""
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        food.delete()
        messages.success(request, 'Food deleted successfully.')
        return redirect('food_list')
    return render(request, 'tracker/admin/food_confirm_delete.html', {'food': food})


@staff_member_required
def user_list(request):
    """List all users for admin"""
    users = User.objects.all().select_related('userprofile')
    return render(request, 'tracker/admin/user_list.html', {'users': users})


@staff_member_required
def user_update(request, user_id):
    """Update user profile"""
    user = get_object_or_404(User, id=user_id)
    profile, created = UserProfile.objects.get_or_create(user=user)
    if request.method == 'POST':
        profile.calorie_goal = int(request.POST.get('calorie_goal', 2000))
        profile.save()
        messages.success(request, 'User profile updated successfully.')
        return redirect('user_list')
    return render(request, 'tracker/admin/user_form.html', {'user': user, 'profile': profile})

