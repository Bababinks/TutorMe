from django.db import models

class tutorMeUser(models.Model):
    email = models.EmailField(unique=True)
    oauth_uid = models.CharField(max_length=255)
    is_tutor = models.BooleanField(default=False)
    is_admin_set = models.BooleanField(default=False)

    # other fields as needed

    def __str__(self):
        return self.email
