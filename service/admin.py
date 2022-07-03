from django.contrib import admin
from .models import Massage, Schedule, Slot


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('therapist', 'client', 'start_time', 'end_time', 'status',)
    list_filter = ('status',)
    search_fields = ('client__username', 'therapist__username',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('therapist', 'translate_days', 'start_time', 'end_time',)
    list_filter = ('therapist',)

    # def has_add_permission(self, request):
    #     return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'therapist', 'start_time', 'end_time',)
    list_filter = ('therapist',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
