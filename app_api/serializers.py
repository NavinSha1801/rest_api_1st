
from rest_framework import serializers
from .models import Post
from django import forms

# class myform(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = {
#             'name','email','phonenumber'
#         }

class myserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = {
            'name','email','phonenumber'
        }
