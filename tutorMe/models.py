from django.db import models

class tutorMeUser(models.Model):
    email = models.EmailField(unique=True)
    is_tutor = models.BooleanField(default=False)
    is_admin_set = models.BooleanField(default=False)
    first_name = models.CharField(default="", max_length=255)
    last_name = models.CharField(default="", max_length=255)

    # other fields as needed
    def __str__(self):
        return self.email

class TutorClasses(models.Model):

    tutor = models.ForeignKey(
        'tutorMeUser',
        on_delete=models.CASCADE,
    )
    mnemonic = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


