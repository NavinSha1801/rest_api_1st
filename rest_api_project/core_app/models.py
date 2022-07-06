from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class post_model(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner =  models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
