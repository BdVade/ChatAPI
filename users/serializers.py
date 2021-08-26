from .models import MyUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username']
