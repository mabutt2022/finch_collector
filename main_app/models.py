from django.db import models
from django.urls import reverse


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

CHAR = (
    ('Feathers', 'Feathers'),
    ('High metabolism', 'High metabolism'),
    ('A four-chambered heart', 'A four-chambered heart'),
    ('A beak with no teeth', 'A beak with no teeth'),
    ('A lightweight but strong skeleton', 'A lightweight but strong skeleton'),
    ('Production of hard-shelled egg', 'Production of hard-shelled egg')
)

LEVEL = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)

# Create your models here.
class Features(models.Model):
    characteristic = models.CharField(max_length=100, choices=CHAR)
    strength = models.CharField(max_length=1, choices=LEVEL, default='1')  

    def __str__(self):
        return f'{self.get_strength_display()} at Strength: {self.strength}'
    
    def get_absolute_url(self):
        return reverse('feature_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    nesting = models.CharField(max_length=100)
    behavior = models.CharField(max_length=100)
    conservation = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    strength = models.ManyToManyField(Features)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField(max_length=100)
    meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    
    # change the default sort
    class Meta:
        ordering = ['-date']