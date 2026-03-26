from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer