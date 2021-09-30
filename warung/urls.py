
from django.contrib import admin
from django.urls import path, include
from warung import views
urlpatterns = [
    path('warung/', views.warungView),
    path('warung/<int:id>', views.warungDetail),
    
]
