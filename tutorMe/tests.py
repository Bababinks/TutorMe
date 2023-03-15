from django.test import TestCase
from .models import tutorMeUser
from .views import TutorView, StudentView
from django.urls import reverse

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

# class viewsTest(TestCase):
#
#     def test_tutorView(self):
#         # x = self.create_user()
#         # y = self.client.get(url)
#         # self.assertEqual(y.status_code, 200)
#         # self.assertIn(x.title, y.content)
#         path = reverse("tutorMe:tutor")
#         request = RequestFactory().get(path)
#         response = TutorView(request)
#         assert response.status_code == 200