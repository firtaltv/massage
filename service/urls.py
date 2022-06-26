from django.urls import path
from .views import (ClientMassageListAPIView,
                    TherapistMassageListAPIView,
                    TherapistScheduleListAPIView,
                    TherapistSlotListAPIView,
                    )

app_name = 'service'

urlpatterns = [
    path('client/', ClientMassageListAPIView.as_view(), name='client_massages_list'),
    path('therapist/', TherapistMassageListAPIView.as_view(), name='therapist_massages_list'),
    path('therapists/<int:pk>/schedule/', TherapistScheduleListAPIView.as_view(), name='therapist_schedule_object'),
    path('therapists/<int:pk>/slot/', TherapistSlotListAPIView.as_view(), name='therapist_slot_list'),
]
