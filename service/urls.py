from django.urls import path
from .views import ClientMassageAPIView, TherapistMassageAPIView

app_name = 'service'

urlpatterns = [
    path('cli', ClientMassageAPIView.as_view(), name='client_massage_list'),
    path('ther', TherapistMassageAPIView.as_view(), name='therapist_massage_list'),
]
