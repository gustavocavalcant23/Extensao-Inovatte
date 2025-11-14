from django.urls import path

from .views import RegisterView, RegisterConfirmationView



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('confirmation/', RegisterConfirmationView.as_view(), name='register_confirmation'),
]