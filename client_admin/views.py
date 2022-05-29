from django.shortcuts import render, redirect
from django.views import generic
from invitations.utils import get_invitation_model
from django.http import HttpResponseNotFound, HttpResponseForbidden
from counselling_appts.models import Appointment

#decorator to redirect non-authenticated users to login page
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def display_appointment_admin(request):
    '''
    Display appointment admin page
    '''
    if request.user.is_superuser:
        appointments = Appointment.objects.all()

        context = {
        'appointments': appointments,
        }

        return render(request, 'client_admin/appointment_admin.html', context)

    else:
        return HttpResponseForbidden("403 error: Unauthorized")

    


@login_required
def display_client_admin(request):
    '''
    Display main client admin page
    '''

    if request.user.is_superuser:
        return render(request, 'client_admin/client_admin.html')
    else:
        return HttpResponseNotFound("404 error: FIle not found")


@login_required
def invite_new_client(request):
    '''
    Display client invitation page
    '''

    if request.user.is_superuser:
        return render(request, 'client_admin/invite_client.html')
    else:
        return HttpResponseNotFound("404 error: FIle not found")


@login_required
def display_invite_confirmation(request):
    '''
    Display invite sent confirmation page
    '''

    if request.user.is_superuser:
        return render(request, 'client_admin/invite_confirmation.html')
    else:
        return HttpResponseNotFound("404 error: FIle not found")


@login_required
def send_invite(request):
    '''
    Send invite to new client
    '''
    
    if request.user.is_superuser:
        if request.method == "POST":
            Invitation = get_invitation_model()
            email = request.POST.get('email')
            invite = Invitation.create(email, inviter=request.user)
            invite.send_invitation(request)

            return redirect(display_invite_confirmation)
    else:
        return HttpResponseNotFound("404 error: FIle not found")


@login_required
def change_appointment_status(request, value):
    '''
    Change appointment status
    '''

    if request.user.is_superuser:
        if request.method == "POST":
            print('hello world')
            print("Item ID: " + appointment_id)
            PRINT("vALUE: " + value )
            return render(request, 'client_admin/appointment_admin.html')

    else:
        return HttpResponseForbidden("403 error: Unauthorized")