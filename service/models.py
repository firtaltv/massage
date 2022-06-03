from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _


class Massage(models.Model):
    class Status(models.TextChoices):
        TBD = 'TBD', _('To be Done')
        IP = 'IP', _('In Progress')
        DN = 'DN', _('Done')

    therapist = models.ForeignKey(
        User, related_name='therapist', on_delete=models.CASCADE
    )
    client = models.ForeignKey(
        User, related_name='client', on_delete=models.CASCADE
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.TBD,
    )

    def __str__(self):
        return f"Therapist: {self.therapist.get_full_name()} " \
               f"| Client: {self.client.get_full_name()} | " \
               f"{self.start_time.strftime('%d %b %Y, from %H:%M')} " \
               f"to {self.end_time.strftime('%H:%M')}"
