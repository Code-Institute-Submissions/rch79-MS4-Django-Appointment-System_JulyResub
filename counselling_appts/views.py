from django.shortcuts import render
from django.views import generic
from .models import Appointment

class HomePageView(generic.TemplateView):
    template_name = 'index.html'


class AppointmentListView(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.all()
    template_name = 'appointments.html'
