from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenViewBase

from .models import User
from .serializers import UserSerializer, LoginSerializer


class UserProfileAPIView(RetrieveUpdateAPIView):
    http_method_names = [
        "get",
        "patch",
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.request.user.pk)
        self.check_object_permissions(self.request, obj)
        return obj


class LoginAPIView(TokenViewBase):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )
