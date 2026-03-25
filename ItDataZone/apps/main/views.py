from rest_framework import permissions
from django.shortcuts import render
from django.views import View


class HomeView(View):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return render(request, 'main/home.html')