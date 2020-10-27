from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
      'id', 'username', 'email', 'first_name', 'last_name'
    )
