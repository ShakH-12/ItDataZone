from rest_framework import generics, permissions
from .serializers import GroupSerializer
from .models import Group


# /api/v1/group/
class GroupView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


# /api/v1/group/<int:pk>/
class GroupDetailView(generics.RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]