from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import RegisterSerializer, ResponseSerializer, UpdateSerializer


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
    queryset = User.objects.filter(is_active=True)
    serializer_class = UpdateSerializer