from django.db import models


class services(models.Model):
    service_for = models.TextField(max_length=100, null=True)
    service_required_on = models.TextField()
    service_required_at = models.CharField(max_length = 100)
    contact = models.IntegerField()
    mail = models.TextField(max_length = 100)
    information = models.CharField(max_length = 100)



class hiring(models.Model):
    name = models.TextField(max_length = 100)
    password = models.TextField(max_length=100, null=True)
    location = models.TextField(max_length = 1000)
    contactno = models.TextField(max_length = 10)
    mail = models.TextField(max_length = 100)
    qualification = models.TextField(max_length = 1000)    
    jobrole = models.TextField(max_length=1000)
    experience = models.TextField(max_length=100)

class signup(models.Model):
    username = models.TextField(max_length = 100)
    email = models.TextField(max_length = 100)
    password = models.TextField(max_length = 100)
