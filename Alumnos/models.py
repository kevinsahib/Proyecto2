from django.db import models


class AlumnosModel(models.Model):

    name = models.CharField(max_length = 100, null = False)
    age = models.CharField(max_length = 100, null = False)
    email = models.CharField(max_length = 80, null = False)   

    def __str__ (self):
        return self.name
