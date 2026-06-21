from django.db import models
from .subcategory import SubCategory


class Recipe(models.Model):
    
    subcategory = models.ForeignKey(
        SubCategory, 
        on_delete=models.CASCADE,
        related_name='recipes'
        )
    title = models.CharField(max_length=120, null=False)
    description = models.TextField()
    instructions = models.TextField()    
    main_image = models.ImageField(upload_to='media/recipes/')

    def __str__(self):
        return self.title
    