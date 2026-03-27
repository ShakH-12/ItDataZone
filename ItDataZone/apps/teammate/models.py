from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Role(models.Model):
    name = models.CharField(verbose_name="Role Name", max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.name


class Teammate(models.Model):
    photo = models.ImageField(verbose_name="Photo")
    full_name = models.CharField(validators=[MinLengthValidator(5)], max_length=100, verbose_name="Full Name", db_index=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Role")
    about = models.TextField(validators=[MaxLengthValidator(1000)], verbose_name="About")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    github_link = models.URLField(verbose_name="Github Link", blank=True, null=True)
    telegram_link = models.URLField(verbose_name="Telegram Link", blank=True, null=True)
    instagram_link = models.URLField(verbose_name="Instagram Link", blank=True, null=True)
    presentation = models.FileField(verbose_name="Presentation", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    date_of_joining = models.DateField(verbose_name="Date of Joining", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["full_name"])]

    def __str__(self):
        return self.full_name