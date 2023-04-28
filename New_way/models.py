from django.db import models

# Create your models here.
class email(models.Model):
    SNO = models.TextField()
    EMAIL =models.EmailField()

class game(models.Model):
    SNO = models.TextField()
    EMAIL =models.EmailField()