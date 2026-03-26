from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from decimal import Decimal


class Course(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(3)], verbose_name="Course Name", db_index=True)
    description = models.TextField(verbose_name="Course Description", db_index=True)
    price = models.DecimalField(validators=[MinValueValidator(Decimal("0.00"))], max_digits=10, decimal_places=2)
    photo = models.ImageField(verbose_name="Course Photo", upload_to="course_images/")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["name", "description"])]

    def __str__(self):
        return self.name

    @property
    def is_expency(self):
        return self.price > 250000

    def deactivate(self):
        self.is_active = False
        self.save(update_fields=["is_active"])

    def activate(self):
        self.is_active = True
        self.save(update_fields=["is_active"])