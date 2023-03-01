from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    nesting = models.CharField(max_length=100)
    behavior = models.CharField(max_length=100)
    conservation = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name