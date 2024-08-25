from django.db import models

# Create your models here.
class Fotos(models.Model):
    name = models.CharField(max_length=128)
    autor = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name