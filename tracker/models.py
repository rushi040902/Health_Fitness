from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Food(models.Model):
    """Food items with nutritional information"""
    name = models.CharField(max_length=200)
    carbs = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    calories = models.FloatField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class UserProfile(models.Model):
    """Extended user profile with calorie goal"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    calorie_goal = models.IntegerField(default=2000)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"


class Consumption(models.Model):
    """Track user's food consumption"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    quantity = models.FloatField(default=1.0)
    
    class Meta:
        ordering = ['-date', '-id']
    
    def __str__(self):
        return f"{self.user.username} - {self.food.name} - {self.date}"
    
    @property
    def total_carbs(self):
        return self.food.carbs * self.quantity
    
    @property
    def total_protein(self):
        return self.food.protein * self.quantity
    
    @property
    def total_fats(self):
        return self.food.fats * self.quantity
    
    @property
    def total_calories(self):
        return self.food.calories * self.quantity

