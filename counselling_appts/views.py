from django.shortcuts import render
from django.views import generic
from .models import Appointment

class HomePageView(generic.TemplateView):
    template_name = 'index.html'


class AppointmentListView(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.all()
    template_name = 'appointments.html'


class MessageView(generic.TemplateView):
    template_name = 'contact.html'


class AppointmentBookingView(generic.TemplateView):
    template_name = 'counselling_appts/appointment_booking.html'
