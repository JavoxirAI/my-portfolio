from django.urls import path
from .views import my_profile, teacher_view

urlpatterns = [
    path('my-profile/', my_profile),
    path('teacher/', teacher_view),
]
