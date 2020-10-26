from django.db import models
from django.contrib.auth.models import User
import json
from django.http import JsonResponse, QueryDict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from api.serializers import UserSerializer



class UserLogin(APIView):
  parser_classes = [JSONParser]

  def get(self, request):
    user = User.objects.get(username=request.data[username])
    
