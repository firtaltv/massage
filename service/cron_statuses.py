from datetime import datetime
from .models import Massage
from django_cron import CronJobBase, Schedule
import pytz

utc = pytz.UTC


class SetStatusJob(CronJobBase):
    """
    Run the job
    """
    RUN_EVERY_MIN = 0.1
    schedule = Schedule(run_every_mins=RUN_EVERY_MIN)
    code = "service.cron_statuses.SetStatusJob"

    @staticmethod
    def set():
        qs_tbd = Massage.objects.filter(status='TBD')
        for obj in qs_tbd:
            if obj.start_time < utc.localize(datetime.now()) < obj.end_time:
                obj.status = 'IP'
                obj.save()
            elif obj.end_time < utc.localize(datetime.now()):
                obj.status = 'DN'
                obj.save()
        qs_ip = Massage.objects.filter(status='IP')
        for obj in qs_ip:
            if obj.end_time < utc.localize(datetime.now()):
                obj.status = 'DN'
                obj.save()

    def do(self):
        self.set()
