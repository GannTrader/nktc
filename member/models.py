from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


GENDER = (
    ('nam', 'nam'),
    ('nữ', 'nữ'),
)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="tagUser")
    avatar = models.FileField(blank=True, null=True)
    gender = models.CharField(max_length=25, choices=GENDER, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.user.username