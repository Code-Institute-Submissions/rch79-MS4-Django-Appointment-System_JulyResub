from datetime import datetime
from django.shortcuts import render, redirect
from django.views import generic

# decorator to redirect non-authenticated users to login page
from django.contrib.auth.decorators import login_required

# python functions used to send date info to the date and time pickers
from .modules.booked_dates import create_appt_dict, create_fully_booked_list, create_available_timeslots


from .models import Appointment, User


class HomePageView(generic.TemplateView):
    template_name = 'index.html'


class MessageView(generic.TemplateView):
    template_name = 'contact.html'


class AppointmentBookingView(generic.TemplateView):
    template_name = 'counselling_appts/appointment_booking.html'



## test view - delete before deployment
class TestView(generic.TemplateView):
    template_name = 'counselling_appts/test_template.html'

@login_required
def display_confirmation_page(request):
    return render(request, 'counselling_appts/confirmation.html')


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


@login_required
def book_appointment(request):
    '''
    Book an appointment based on available slots
    '''

    if request.method == "GET":
        dates_dict = create_appt_dict()
        time_slots = create_available_timeslots(dates_dict)
        blocked_dates = create_fully_booked_list(dates_dict)

        context = {
            'dates_dict': dates_dict,
            'blocked_dates': blocked_dates,
            'time_slots': time_slots,
        }

    return render(request, 'counselling_appts/appointment_booking.html', context)


@login_required
def confirm_appointment(request):
    '''
    Create new Appointment object
    '''

    if request.method == "POST":
        time = request.POST.get("time")
        date = request.POST.get("date")
        datetime_str = date + " " + time
        appt_date = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        client = request.user
        Appointment.objects.create(client=client, date=appt_date, status=1)

        return redirect(display_confirmation_page)


