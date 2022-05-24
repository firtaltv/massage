from django.db import models
from users.models import User

MASSAGE_STATUSES = [
    ('TBD', 'To be Done'),
    ('IP', 'In Progress'),
    ('DN', 'Done'),
]


class Massage(models.Model):
    therapist_id = models.ForeignKey(User, null=False, related_name='Therapist', on_delete=models.CASCADE)
    client_id = models.ForeignKey(User, null=False, related_name='Client', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(
        max_length=10,
        choices=MASSAGE_STATUSES,
        default='TBD',
    )
