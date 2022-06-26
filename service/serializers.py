from rest_framework import serializers
from users.models import User
from .models import Massage, Schedule, Slot


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'pk',
            'last_name',
            'first_name',
        )


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = (
            'pk',
            'therapist',
            'client',
            'start_time',
            'end_time',
            'status',
        )
        read_only_fields = (
            'therapist',
            'client',
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['therapist'] = UserSerializer(instance.therapist).data
        ret['client'] = UserSerializer(instance.client).data
        return ret


class ScheduleSerializer(serializers.ModelSerializer):
    weekdays = {
        '0': 'Monday',
        '1': 'Tuesday',
        '2': 'Wednesday',
        '3': 'Thursday',
        '4': 'Friday',
        '5': 'Saturday',
        '6': 'Sunday',
    }
    class Meta:
        fields = (
            'pk',
            'days',
            'therapist',
            'start_time',
            'end_time',
        )
        model = Schedule
        read_only_fields = (
            'therapist',
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['days'] = [self.weekdays.get(i) for i in ret['days']]
        ret['therapist'] = UserSerializer(instance.therapist).data
        return ret


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'pk',
            'schedule',
            'therapist',
            'start_time',
            'end_time',
        )
        model = Slot
        read_only_fields = (
            'therapist',
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['schedule'] = ScheduleSerializer(instance.schedule).data
        ret.pop('therapist')
        return ret
