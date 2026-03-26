from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, RegisteredUser
from .serializers import RegisterSerializer, ResponseSerializer, UpdateSerializer, RegisterToCourseSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(ResponseSerializer(user).data)


class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.filter()
    serializer_class = UpdateSerializer


class RegisterToCourseView(generics.CreateAPIView):
    queryset = RegisteredUser.objects.filter()
    serializer_class = RegisterToCourseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(RegisterToCourseSerializer(user).data)