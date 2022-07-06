from django.contrib import admin

# Register your models here.
from .models import post_model

admin.site.register(post_model)
