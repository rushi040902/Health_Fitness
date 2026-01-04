from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add-food/', views.add_food, name='add_food'),
    path('remove-food/<int:consumption_id>/', views.remove_food, name='remove_food'),
    path('update-goal/', views.update_calorie_goal, name='update_goal'),
    path('search-foods/', views.search_foods, name='search_foods'),
]

