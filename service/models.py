from datetime import datetime, timedelta

import pytz
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.forms import MultipleChoiceField
from django.utils.translation import gettext_lazy as _

from users.models import User

utc = pytz.UTC


class Massage(models.Model):
    class Status(models.TextChoices):
        TODO = 'TODO', _('To Do')
        INPROG = 'INPROG', _('In Progress')
        DONE = 'DONE', _('Done')

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
        default=Status.TODO,
    )


class ChoiceArrayField(ArrayField):
    """ Helper for multiple choice field """

    def formfield(self, **kwargs):
        defaults = {
            'form_class': MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        return super(ArrayField, self).formfield(**defaults)


class Schedule(models.Model):

    class Week(models.TextChoices):
        Monday = 0, _('Monday')
        Tuesday = 1, _('Tuesday')
        Wednesday = 2, _('Wednesday')
        Thursday = 3, _('Thursday')
        Friday = 4, _('Friday'),
        Saturday = 5, _('Saturday'),
        Sunday = 6, _('Sunday'),

    days = ChoiceArrayField(
        base_field=models.CharField(max_length=10, choices=Week.choices),
        default=list,
        size=10,
        blank=True,
    )
    therapist = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_approved = models.BooleanField(default=False)

    @property
    def translate_days(self):
        """ Translates weekday number into word """
        return [Schedule.Week.choices[int(item)][1] for item in self.days]

    def __str__(self):
        return f'{self.therapist.username}\'s schedule'

    @staticmethod
    def relative_date(reference, weekday, timevalue):
        hour, minute = divmod(timevalue, 1)
        minute *= 60
        days = reference.weekday() - weekday
        return (reference - timedelta(days=days)).replace(
            hour=int(hour), minute=int(minute), second=0, microsecond=0)

    def create_slots(self, weeks=4):
        slots_list = list()
        for item in Schedule.objects.filter(is_approved=True):
            days = list(map(int, item.days))
            time_from = datetime.now() if not Slot.objects.all() \
                else Slot.objects.filter(schedule=item).order_by(end_time)[-1].end_time
            if datetime.now().weekday() < any(days):
                days[:] = [day for day in days if day < datetime.now().weekday()]
                for day in days:
                    weekday_number = day
                    for week in range(weeks):
                        slots_list.append(
                            {
                                'start_time': self.relative_date(time_from, int(weekday_number),
                                                                 int(item.start_time.strftime("%H"))),
                                'end_time': self.relative_date(time_from, int(weekday_number),
                                                               int(item.end_time.strftime("%H"))),
                                'therapist': item.therapist,
                                'schedule': item
                            }
                        )
                        weekday_number += 7
            else:
                for day in days:
                    weekday_number = day + 7
                    for week in range(weeks - 1):
                        slots_list.append(
                            {
                                'start_time': self.relative_date(time_from, int(weekday_number),
                                                                 int(item.start_time.strftime("%H"))),
                                'end_time': self.relative_date(time_from, int(weekday_number),
                                                               int(item.end_time.strftime("%H"))),
                                'therapist': item.therapist,
                                'schedule': item
                            }
                        )
                        weekday_number += 7
        obj_list = [Slot(**data_dict) for data_dict in slots_list]
        objs = Slot.objects.bulk_create(obj_list)


class Slot(models.Model):
    schedule = models.ForeignKey(Schedule, related_name='schedule', on_delete=models.CASCADE)
    therapist = models.ForeignKey(User, related_name='therapists_schedule', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
