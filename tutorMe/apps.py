from django.apps import AppConfig
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from tutorMe.models import Appointment, Notification


class TutormeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tutorMe'


def generateRejectionMsg(app):
    tutor = app.tutor.first_name + app.tutor.last_name
    class_name = app.class_name
    msg = Notification.objects.create(state=Notification.requestState.REJ, tutor=tutor, class_name=class_name)


@receiver(pre_delete, sender=Appointment)
def initiateMessage(sender, instance):
    """

    :param sender:
    :param instance:
    """
    generateRejectionMsg(sender)
