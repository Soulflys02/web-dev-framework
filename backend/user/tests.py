from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class UserAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('userView')
        self.user = {
            'username': 'testUser',
            'password': 'password',
            'email': 'test@user.com',
            'first_name': 'firstName',
            'last_name': 'lastName',
        }

    
    def test_register_user(self):
        """
        Ensure that we can create an user
        """
        # Request
        response = self.client.post(self.url, self.user)
        self.assertEqual(response.status_code, HTTP_200_OK)

        # Check user is correctly created
        user = User.objects.get(username='testUser')
        self.assertEqual(user.username, self.user['username'])
        self.assertTrue(user.check_password(self.user['password']))
        self.assertEqual(user.email, self.user['email'])
        self.assertEqual(user.first_name, self.user['first_name'])
        self.assertEqual(user.last_name, self.user['last_name'])

    def test_register_user_username_password(self):
        """
        Ensure that we can create an user only with username and password
        """
        # Request
        response = self.client.post(self.url, {'username': self.user['username'], 'password': self.user['password']})
        self.assertEqual(response.status_code, HTTP_200_OK)

        # Check user is correctly created
        user = User.objects.get(username='testUser')
        self.assertEqual(user.username, self.user['username'])
        self.assertTrue(user.check_password(self.user['password']))
        self.assertEqual(user.email, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')
    
    def test_register_user_with_super(self):
        """
        Ensure that we can't create super user and staff user
        """
        data = self.user
        data['is_superuser'] = True
        data['is_staff'] = True
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
    
    def test_user_already_exist(self):
        """
        Ensure that we can't create two user with the same username
        """
        self.client.post(self.url, self.user)
        response = self.client.post(self.url, self.user)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)