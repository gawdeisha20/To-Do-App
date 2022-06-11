from django.contrib import admin
from django.urls import path, include
from .views import taskList

urlpatterns = [
    path('add-item/', taskList.as_view()),
    path('del-items/<int:id>', taskList.as_view())
]
