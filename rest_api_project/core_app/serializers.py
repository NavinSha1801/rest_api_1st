from rest_framework import serializers

from .models import post_model


class Form(serializers.ModelSerializer):
    class Meta:
        model = post_model
        fields = (
            'name','email','phone','owner'
        ) 