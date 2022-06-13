from datetime import datetime
from .models import Massage, Slot, Schedule
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
        qs = Massage.objects.all()
        for obj in qs:
            if obj.status == 'TBD':
                if obj.start_time < utc.localize(datetime.now()) < obj.end_time:
                    obj.status = 'IP'
                    obj.save()
                elif obj.end_time < utc.localize(datetime.now()):
                    obj.status = 'DN'
                    obj.save()
            if obj.status == 'IP':
                if obj.end_time < utc.localize(datetime.now()):
                    obj.status = 'DN'
                    obj.save()

    def do(self):
        self.set()
