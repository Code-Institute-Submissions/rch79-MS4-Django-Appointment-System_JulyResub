from django.shortcuts import render
from django.views import generic

#decorator to redirect non-authenticated users to login page
from django.contrib.auth.decorators import login_required

from .models import Appointment, User

class HomePageView(generic.TemplateView):
    template_name = 'index.html'


class MessageView(generic.TemplateView):
    template_name = 'contact.html'


class AppointmentBookingView(generic.TemplateView):
    template_name = 'counselling_appts/appointment_booking.html'

class TestView(generic.TemplateView):
    template_name = 'counselling_appts/test_template.html'

@login_required
def list_appointments(request):
    """
    Displays scheduled appointments for logged in clients
    Superusers ill be shown all scheduled appointments
    for all clients
    """

    if request.user.is_superuser:
        appointments = Appointment.objects.all()
    else:
        appointments = Appointment.objects.filter(client__exact=request.user)

    context = {
        'appointments': appointments,
    }

    return render(request, 'counselling_appts/appointments.html', context)