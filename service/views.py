from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Massage, Schedule, Slot
from .serializers import MassageSerializer, ScheduleSerializer, SlotSerializer


class ClientMassageListAPIView(ListAPIView):
    """ Get list of all massages for current logged in client """
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(client=self.request.user)


class TherapistMassageListAPIView(ListAPIView):
    """ Get list of all massages for current logged in therapist """
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(therapist=self.request.user)


class TherapistScheduleAPIView(RetrieveAPIView):
    """ Get schedule for any Therapist """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return super().get_queryset().filter(therapist__id=pk)

    def get_object(self):
        return super().get_object()


class TherapistSlotListAPIView(ListAPIView):
    """ Get list of all slots for any therapist """
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return super().get_queryset().filter(therapist__id=pk)
