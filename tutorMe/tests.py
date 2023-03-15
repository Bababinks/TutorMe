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

    def test_userCreated(self):
        x = self.create_user()
        self.assertTrue(isinstance(x, tutorMeUser))

    def test_userStudent(self):
        x = self.create_user()
        self.assertEqual(x.is_tutor, False)

    def test_userTutorAttributes(self):
        x = self.create_user()
        x = tutorMeUser(email='1234@gmail.com', first_name='john', last_name='doe', is_tutor=True)
        self.assertEqual(x.is_tutor, True)
        self.assertEqual(x.email, '1234@gmail.com')
        self.assertEqual(x.first_name, 'john')
        self.assertEqual(x.last_name, 'doe')


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