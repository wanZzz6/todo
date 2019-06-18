from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home),
    path('edit/', views.edit),
    path('about/', views.about)
]