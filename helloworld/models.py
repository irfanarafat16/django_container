from django.db import models

# Create your models here.
class DataModel(models.Model):
    name = models.CharField(max_length = 200)
    address = models.TextField()

    def __str__(self):
        return self.title

