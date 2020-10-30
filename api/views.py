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
from rest_framework.permissions import IsAuthenticated 



class UserLogin(APIView):
  parser_classes = [JSONParser]

  def post(self, request):
    user = User.objects.get(username=request.data['username'])
    if user is None :
        return Response('Username not Found') 
    if user.check_password(request.data['password']) :
        return Response(UserSerializer(user).data)
    else :
        return Response('Incorrect Password')

class UserDetail(APIView):
  parser_classes = [JSONParser]

  def post(self, request):
    try:
        User.objects.get(username=request.data['username'])
    except User.DoesNotExist:
        user = User.objects.create_user(username=request.data['username'], email=request.data['email'], password=request.data['password'], first_name=request.data['first_name'], last_name=request.data['last_name'])
        return Response(UserSerializer(user).data)
    return Response('Username Already Exists')
  

