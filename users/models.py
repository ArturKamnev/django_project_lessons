from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomUser(User):
    photo = models.ImageField(upload_to='users/')
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=100, default='m')

    def __str__(self):
        return self.username