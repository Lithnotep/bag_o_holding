from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):
    def test_user_create(self):
        user = User.objects.create_user(username='Morra', email='test.com', password='password', first_name='Milly', last_name='Manny')
        self.assertEqual(user.username, 'Morra')
        self.assertEqual(user.email, 'test.com')
        self.assertEqual(user.first_name, 'Milly')
        self.assertEqual(user.last_name, 'Manny')