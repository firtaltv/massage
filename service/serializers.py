from rest_framework import serializers
from users.models import User
from .models import Massage


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
