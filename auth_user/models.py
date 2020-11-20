from django.db import models
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class auth_userModel(models.Model):
    
    password = models.CharField(max_length = 128, null = False)
    username = models.CharField(max_length = 150, null = False)
    first_name = models.CharField(max_length = 150, null = False)
    last_name = models.CharField(max_length = 150, null = False)
    email = models.CharField(max_length = 254, null = False)

    def __str__ (self):
        return self.username