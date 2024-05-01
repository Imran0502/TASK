from django.db import models

# Create your models here.
from django.db import models

class FoodRecipe(models.Model):
    food_type_choice = [
        ('VEG', 'Vegetarian'),
        ('NON-VEG', 'Non-Vegetarian'),
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    ingredients = models.CharField(max_length=1000)
    method = models.CharField(max_length=1000)
    category = models.CharField(max_length=10, choices=food_type_choice)
    
    
    def __str__(self):
        return self.name
