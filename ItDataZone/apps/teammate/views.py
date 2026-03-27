from rest_framework import generics
from .models import Teammate
from .serializers import TeammateSerializer


class TeammateList(generics.ListCreateAPIView):
    queryset = Teammate.objects.all()
    serializer_class = TeammateSerializer