from django.urls import path 
from .views import Quiz_all,Topic_all

urlpatterns = [
    path('quiz/', Quiz_all.as_view()),
    path('topic/<int:pk>/', Topic_all.as_view()),
]