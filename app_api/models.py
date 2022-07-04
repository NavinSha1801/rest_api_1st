from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name