from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeammateList.as_view()),
]