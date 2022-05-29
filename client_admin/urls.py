from . import views
from django.urls import path


urlpatterns = [
    path('', views.display_client_admin, name='display_client_admin'),
    path('new_invite/', views.invite_new_client, name='invite_new_client'),
    path('new_invite/send', views.send_invite, name='send_invite'),
    path('new_invite/sent', views.display_invite_confirmation, name='display_invite_confirmation'),
    path('appointment_admin/', views.display_appointment_admin, name='appointment_admin'),
    path('change/<appointment_id>', views.change_appointment_status, name='change'),
]
