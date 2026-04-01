from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view()),
    path("profile/", views.ProfileView.as_view()),
    path("student/", views.StudentView.as_view()),
    path("student/<int:pk>/", views.StudentDetailView.as_view()),
]