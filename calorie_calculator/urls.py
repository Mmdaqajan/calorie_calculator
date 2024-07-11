from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calculate_calorie, name='calculate_page')
]