from django.test import TestCase
from django.contrib.auth import get_user_model

class FS_UserManagerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='testuser@gmail.com', username='jeff', password='password123')
        self.assertEqual(user.email, 'testuser@gmail.com')
        self.assertEqual(user.username, 'jeff')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(email='testuser@gmail.com', username='jeff', password='password123')
        self.assertEqual(user.email, 'testuser@gmail.com')
        self.assertEqual(user.username, 'jeff')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_admin)
        self.assertTrue(user.is_superuser)
