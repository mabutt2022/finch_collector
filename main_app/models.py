from django.db import models
from django.urls import reverse

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
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField(max_length=100)
    meal = models.CharField(max_length=100)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_desplay()} on {self.date}'