from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.user.views import PageNotFoundView

handler404 = 'apps.user.views.custom_404'

urlpatterns = [
    path("6cUzHRjpuLeURg/", admin.site.urls),
    path("", include("apps.main.urls")),

    path("api/v1/user/", include("apps.user.urls")),
    path("api/v1/bot/", include("apps.bot.urls")),
    path("api/v1/course/", include("apps.course.urls")),
    path("api/v1/teammate/", include("apps.teammate.urls")),
    path("api/v1/group/", include("apps.group.urls")),

    path("api/token/", TokenObtainPairView.as_view()),
    path("api/refresh/", TokenRefreshView.as_view()),


    path("<first>/", PageNotFoundView.as_view()),
    path("<first>/<second>/", PageNotFoundView.as_view()),
    path("<first>/<second>/<third>/", PageNotFoundView.as_view()),
    path("<first>/<second>/<third>/<fifth>/", PageNotFoundView.as_view()),
    path("<first>/<second>/<third>/<fifth>/<sixth>/", PageNotFoundView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)