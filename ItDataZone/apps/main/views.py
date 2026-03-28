from rest_framework import permissions
from django.shortcuts import render
from django.views import View
from ..teammate.models import Teammate, Certificate
from ..course.models import Course


class HomeView(View):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        courses = Course.objects.filter(is_active=True)
        return render(request, 'main/home.html', {"courses": courses})


class TeammatesView(View):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        teammates = Teammate.objects.filter(is_active=True)
        return render(request, 'main/teammates.html', {'teammates': teammates})


class CertificatesView(View):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        certificates = Certificate.objects.all()
        return render(request, 'main/certificates.html', {'certificates': certificates})


class RuHomeView(View):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        courses = Course.objects.filter(is_active=True)
        return render(request, 'main/ru/home.html', {"courses": courses})


class RuTeammatesView(View):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        teammates = Teammate.objects.filter(is_active=True)
        return render(request, 'main/ru/teammates.html', {'teammates': teammates})