from django.contrib import admin
from .models import Massage


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    readonly_fields = (
        'therapist_id',
        'client_id',
        'start_time',
        'end_time',
        'status',
    )
