from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home, name='主页'),
    path('edit/', views.edit, name='编辑'),
    path('about/', views.about, name='关于')
]