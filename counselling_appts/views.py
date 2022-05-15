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
    template_name = 'appointment_booking.html'


class SignOut(generic.TemplateView):
    template_name = 'allauth/account/logout.html'


class SignIn(generic.TemplateView):
    template_name = 'allauth/account/login.html'
