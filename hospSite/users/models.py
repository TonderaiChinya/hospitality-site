from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    date_of_birth = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} Profile'