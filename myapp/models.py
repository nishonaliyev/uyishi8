from django.db import models
from django.contrib.auth.models import User
class Menu(models.Model):
    resturant_img = models.ImageField()
    name_restorant = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name_restorant
   


