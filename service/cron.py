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
        qs = Massage.objects.filter(
            status='TBD',
            start_time__lt=utc.localize(datetime.now())
        ).update(status='IP')
        qsip = Massage.objects.filter(
            status="IP",
            end_time__lt=utc.localize(datetime.now())
        ).update(status='DN')
        Massage.objects.bulk_update(qs, update_fields=["status"])
        Massage.objects.bulk_update(qsip, update_fields=["status"])

    def do(self):
        self.set()
