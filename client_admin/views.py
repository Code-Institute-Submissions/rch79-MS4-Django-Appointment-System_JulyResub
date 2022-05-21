from django.shortcuts import render
from django.views import generic
from invitations.utils import get_invitation_model


# Create your views here.


class ClientAdminPageView(generic.TemplateView):
    template_name = 'client_admin/client_admin.html'

class InviteClientPageView(generic.TemplateView):
    template_name = 'client_admin/invite_client.html'

class AppointmentAdminPageView(generic.TemplateView):
    template_name = 'client_admin/appointment_admin.html'