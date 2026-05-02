from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, EmailOTP


@receiver(post_save, sender=User)
def create_user_profile_and_otp(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        EmailOTP.objects.create(user=instance, otp="000000")