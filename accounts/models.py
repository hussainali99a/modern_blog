from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profiles/", default="profiles/default.png")
    location = models.CharField(max_length=150, blank=True)
    website = models.URLField(blank=True)
    tags = models.CharField(max_length=255, blank=True)
    profession = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.user.username


class EmailOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.user.email} - {self.otp}"