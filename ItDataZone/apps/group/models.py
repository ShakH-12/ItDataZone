from django.db import models
from django.contrib.auth.models import User
from ..teammate.models import Teammate
from ..user.models import Student


class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    mentor = models.ForeignKey(Teammate, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='groups', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        ordering = ['-created_at']

    def __str__(self):
        return self.mentor.full_name