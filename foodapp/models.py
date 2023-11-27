from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Foods(models.Model):
    image = models.ImageField()
    name_food = models.CharField(max_length=50)
    retsep = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name_food