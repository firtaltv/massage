from rest_framework import serializers

from .models import Massage


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = (
            'therapist_id',
            'client_id',
            'start_time',
            'end_time',
            'status',
        )
        read_only_fields = (
            'therapist_id',
            'client_id',
        )
