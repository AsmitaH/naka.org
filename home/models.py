from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    #user = models.OneToOneField(User)
    user = models.OneToOneField('auth.User', related_name='profile')
    mobile = models.IntegerField()
