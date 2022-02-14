from django.shortcuts import render
from django.views import generic
from .models import Appointment


class AppointmentListView(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.all()
    template_name = 'appointments.html'


