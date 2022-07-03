from django.urls import path
from .views import (ClientMassageListAPIView,
                    TherapistMassageListAPIView,
                    TherapistScheduleAPIView,
                    TherapistSlotListAPIView,
                    )

app_name = 'service'

urlpatterns = [
    path('massages/client/', ClientMassageListAPIView.as_view(), name='client_massages_list'),
    path('massages/therapist/', TherapistMassageListAPIView.as_view(), name='therapist_massages_list'),
    path('therapists/<int:pk>/schedule/', TherapistScheduleAPIView.as_view(), name='therapist_schedule_object'),
    path('therapists/<int:pk>/slot/', TherapistSlotListAPIView.as_view(), name='therapist_slot_list'),
]
