from django.shortcuts import render,redirect
from rest_framework import request
from rest_framework import viewsets
from .models import FoodRecipe
from .serializers import FoodRecipeSerializer


# Create your views here.

class recipeView(viewsets.ModelViewSet):
    
    serializer_class = FoodRecipeSerializer
    def get_queryset(self):
        self.queryset = FoodRecipe.objects.all()
        
        recipe_type = self.request.query_params.get('recipe_type')
        if recipe_type:
            self.queryset = self.queryset.filter(category=recipe_type)
        return self.queryset
    
    
        
    
    
