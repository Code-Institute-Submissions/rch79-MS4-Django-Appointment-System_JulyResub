from django.shortcuts import render
from django.views import generic
from .models import Appointment


class AppointmentList(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.filter(status=1).order_by('-date')
    template_name = 'index.html'
