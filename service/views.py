from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import MassageSerializer


class MassageAPIView(RetrieveAPIView):
    http_method_names = [
        'get'
    ]
    queryset = User.objects.all()
    serializer_class = MassageSerializer
    permission_classes = (IsAuthenticated,)
