from datetime import datetime
from .models import Massage
from django_cron import CronJobBase, Schedule
import pytz

utc = pytz.UTC


class SetStatusJob(CronJobBase):
    """
    Set current massage status
    """
    RUN_EVERY_MIN = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MIN)
    code = "service.cron.SetStatusJob"

    @staticmethod
    def set():
        Massage.objects.exclude(status=Massage.Status.TODO).filter(
            start_time__gt=utc.localize(datetime.now())
        ).update(status=Massage.Status.TODO)
        Massage.objects.exclude(status=Massage.Status.INPROG).filter(
            start_time__lt=utc.localize(datetime.now()),
            end_time__gt=utc.localize(datetime.now())
        ).update(status=Massage.Status.INPROG)
        Massage.objects.exclude(status=Massage.Status.DONE).filter(
            end_time__lt=utc.localize(datetime.now())
        ).update(status=Massage.Status.DONE)

    def do(self):
        self.set()
