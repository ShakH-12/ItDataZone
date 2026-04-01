from django.urls import path
from . import views

app_name = 'group'

urlpatterns = [
    path('', views.GroupView.as_view(), name='group'),
    path('<int:pk>/', views.GroupDetailView.as_view(), name='detail'),
]