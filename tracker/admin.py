from django.contrib import admin
from .models import Food, UserProfile, Consumption


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'carbs', 'protein', 'fats', 'calories']
    search_fields = ['name']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'calorie_goal']


@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'food', 'date', 'quantity']
    list_filter = ['date', 'user']
    search_fields = ['user__username', 'food__name']

