from django.urls import path
from .views import ClientMassageAPIView, TherapistMassageAPIView

app_name = 'service'

urlpatterns = [
    path('client/', ClientMassageAPIView.as_view(), name='client_massages_list'),
    path('therapist/', TherapistMassageAPIView.as_view(), name='therapist_massages_list'),
]
