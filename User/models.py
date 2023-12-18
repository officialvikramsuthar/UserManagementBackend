from django.db import models

from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.firstname
    
class RequestLog(models.Model):
    timestamp = models.DateTimeField()
    endpoint = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    status = models.PositiveIntegerField()
