from django.db import models

# Create your models here.
class Linkedin(models.Model):
    clientId = models.CharField(max_length=100)
    code =  models.CharField(max_length=500)
    redirectUri = models.CharField(max_length=200)

    def __str__(self):
        return self.code
