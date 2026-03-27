from django.db import models
from ..course.models import Course


class User(models.Model):
    username = models.CharField(max_length=100, verbose_name="Telegram User username", db_index=True, null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name="Telegram User first name", null=True, blank=True)
    last_name = models.CharField(max_length=100, verbose_name="Telegram User last name", null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name="Telegram User phone number", db_index=True, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Is active")
    is_staff = models.BooleanField(default=False, verbose_name="Is staff")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["is_active"])]

    # def clean(self, *args, **kwargs):
    #     self.full_clean()
    #     super().save(*args, **kwargs)

    def deactivate(self):
        self.is_active = False
        self.save(update_fields=["is_active"])

    def activate(self):
        self.is_active = True
        self.save(update_fields=["is_active"])


class RegisteredUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User", db_index=True)
    full_name = models.CharField(max_length=100, verbose_name="Full name", db_index=True)
    phone = models.CharField(max_length=100, verbose_name="Telegram User phone number", db_index=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course", db_index=True)
    course_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Course Price", db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.course.name}"

    class Meta:
        verbose_name = "Registered User"
        verbose_name_plural = "Registered Users"
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["user", "full_name", "phone", "course"])]