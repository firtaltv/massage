from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Massage
from .serializers import MassageSerializer


class ClientMassageAPIView(ListAPIView):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(client=self.request.user)


class TherapistMassageAPIView(ListAPIView):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(therapist=self.request.user)

