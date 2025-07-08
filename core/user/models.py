from django.db import models
from django.contrib.auth.models import AbstractUser

role_choices = [
    ("participant", "participant"),
    ("admin", "Admin"),
    ("company", "company"),
]


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50, default="user", choices=role_choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Participant(models.Model):
    password = None
    username = None
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, default="participant", choices=role_choices)
    education_level = models.CharField(max_length=255, null=True)
    track = models.CharField(max_length=255, null=True)
