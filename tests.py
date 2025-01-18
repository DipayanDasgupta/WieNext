from django.test import TestCase
from .models import CustomUser

class CustomUserTests(TestCase):
    def test_user_creation(self):
        # Ensure the CustomUser model has a create_user method
        self.assertTrue(hasattr(CustomUser.objects, 'create_user'), "CustomUser model must have a create_user method")
        user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')
