from django.db import models
from django.forms import MultipleChoiceField
from users.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timedelta
import pytz

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

    weekdays_field = {
        '0': 'Monday',
        '1': 'Tuesday',
        '2': 'Wednesday',
        '3': 'Thursday',
        '4': 'Friday',
        '5': 'Saturday',
        '6': 'Sunday',
    }

    @property
    def translate_days(self):
        """ Translates weekday number into word """
        a = [self.weekdays_field.get(str(day)) for day in self.days]
        return a

    therapist = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    @staticmethod
    def create_slots():
        for item in Schedule.objects.all():
            today = datetime.now().weekday()
            this_week = datetime.now() - timedelta(days=today)
            for day in range(len(item.days)):
                sttime = datetime.combine(date=datetime.date(this_week + timedelta(days=int(item.days[day]))),
                                          time=item.start_time)
                endtime = datetime.combine(date=datetime.date(this_week + timedelta(days=int(item.days[day]))),
                                           time=item.end_time)
                for i in range(4):
                    Slot.objects.get_or_create(
                        schedule=item,
                        therapist=item.therapist,
                        start_time=utc.localize(sttime + timedelta(weeks=i)),
                        end_time=utc.localize(endtime + timedelta(weeks=i)),
                    )

    def __str__(self):
        return f'{self.therapist.username}\'s schedule'


class Slot(models.Model):
    schedule = models.ForeignKey(Schedule, related_name='schedule', on_delete=models.CASCADE)
    therapist = models.ForeignKey(User, related_name='therapists_schedule', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
