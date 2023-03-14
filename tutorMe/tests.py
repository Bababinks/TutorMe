from django.test import TestCase
from .models import tutorMeUser

# Create your tests here.

class userTest(TestCase):

    def create_user(self):
        user = tutorMeUser.objects.create()
        user.save()
        return user

    def test_user(self):
        x = self.create_user()
        self.assertTrue(isinstance(x, tutorMeUser))
        self.assertEqual(x.is_tutor, False)
