from django.db import models

class Certificates(models.Model):
    name = models.CharField(max_length=100)
    org = models.CharField(max_length=100)
    date = models.DateField()
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
