from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('teammates/', views.TeammatesView.as_view(), name='teammates'),
    path('certificates/', views.CertificatesView.as_view(), name='certificates'),

    path('ru/', views.RuHomeView.as_view(), name='ru_home'),
    path('ru/teammates/', views.RuTeammatesView.as_view(), name='ru_teammates'),
]