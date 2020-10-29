import json
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

class UserViewSet(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='Morra', email='test.com', password='password', first_name='Milly', last_name='Manny')

    def test_login_user(self):
        data = {
                'username': 'Morra',
                'password': 'password'
                }
        
        response = self.client.post('/api/v1/login/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.user1.id)
        self.assertEqual(response.data['first_name'], self.user1.first_name)
    
    def test_login_user_doesnt_exist(self):
        data = {
                'username': 'dorra',
                'password': 'password'
                }
        
        response = self.client.post('/api/v1/login/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'Username not Found')

    def test_login_user_bad_password(self):
        data = {
                'username': 'Morra',
                'password': 'passord'
                }
        
        response = self.client.post('/api/v1/login/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'Incorrect Password')
    
    def test_create_user(self):
        data = {
            "username": "Mikey",
            "email": "best.com",
            "password": "password",
            "first_name": "Michael",
            "last_name": "Toony"
        }
        
        response = self.client.post('/api/v1/users/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 3)
        self.assertEqual(response.data['username'], "Mikey")
        self.assertEqual(response.data['email'], "best.com")
        self.assertEqual(response.data['first_name'], "Michael")
        self.assertEqual(response.data['last_name'], "Toony")
    
    def test_fail_to_create_user(self):
        data = {
            "username": "Morra",
            "email": "best.com",
            "password": "password",
            "first_name": "Michael",
            "last_name": "Toony"
        }
        
        response = self.client.post('/api/v1/users/', data=data, content_type='application/json')
        self.assertEqual(response.data, 'Username Already Exists')
    
    def test_get_user(self):
        response = self.client.post('/api/v1/users/%s' % self.user1.id, data=data, content_type='application/json')
        
       
  
        
        
        

        