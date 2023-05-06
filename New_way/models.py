from django.db import models


class services(models.Model):
    service_required_on = models.TextField()
    service_required_at = models.CharField(max_length = 100)
    contact = models.IntegerField()
    mail = models.TextField(max_length = 100)
    information = models.CharField(max_length = 100)



class hiring(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 1000)
    contactno = models.CharField(max_length = 10)
    mail = models.CharField(max_length = 100)
    qualification = models.CharField(max_length = 1000)    
    jobrole = models.CharField(max_length=1000)
    experience = models.CharField(max_length=100)

class signup(models.Model):
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
