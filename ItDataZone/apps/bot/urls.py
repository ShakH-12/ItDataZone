from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view()),
    path("update/<int:pk>/", views.UpdateUserView.as_view()),
]