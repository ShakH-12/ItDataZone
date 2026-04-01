from django.db import models


class Student(models.Model):
    fio = models.CharField(max_length=100, verbose_name="Fio")
    email = models.EmailField(null=True, blank=True, verbose_name="Email")
    phone = models.CharField(max_length=100, verbose_name="Phone")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    join_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['-created_at']

    def __str__(self):
        return self.fio