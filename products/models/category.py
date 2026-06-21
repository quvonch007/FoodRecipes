from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=150, null=False)
    image = models.ImageField(upload_to='products/media/')

    def __str__(self):
        return self.name
    
