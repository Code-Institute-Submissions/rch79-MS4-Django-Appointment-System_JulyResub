from . import views
from django.urls import path


urlpatterns = [
    path('appointments', views.AppointmentListView.as_view(), name='appointments')
]
