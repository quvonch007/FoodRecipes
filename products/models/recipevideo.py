from django.db import models
from .recipe import Recipe


class RecipeVideo(models.Model):
    
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='videos'
        )
    video_url = models.URLField()
    
    

    def __str__(self):
        return f"{self.recipe.title} - video"
    
