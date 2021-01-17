from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    date_of_birth = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    location = models.CharField(max_length=50, default='My Location')
    biography = models.CharField(max_length=2000,default='My biography')

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)