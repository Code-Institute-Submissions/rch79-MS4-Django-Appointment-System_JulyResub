from django.shortcuts import render
from django.views import generic

#redirects non-authenticated users to login page
from django.contrib.auth.decorators import login_required

from .models import Appointment, User

class HomePageView(generic.TemplateView):
    template_name = 'index.html'


# class AppointmentListView(generic.ListView):
#     model = Appointment
#     queryset = Appointment.objects.all()
#     template_name = 'appointments.html'


class MessageView(generic.TemplateView):
    template_name = 'contact.html'


class AppointmentBookingView(generic.TemplateView):
    template_name = 'counselling_appts/appointment_booking.html'

@login_required
def list_appointments(request):
    """
    Displays scheduled appointments for logged in clients
    Superusers ill be shown all scheduled appointments
    for all clients
    """

    # client = get_object_or_404(request.user)

    if request.user.is_superuser:
        appointments = Appointment.objects.all()
    else:
        appointments = Appointment.objects.filter(client__exact=request.user)

    context = {
        'appointments': appointments,
    }

    return render(request, 'counselling_appts/appointments.html', context)