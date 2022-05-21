from . import views
from django.urls import path


urlpatterns = [
    path('', views.ClientAdminPageView.as_view(), name='client_admin'),
    path('new_invite/', views.InviteClientPageView.as_view(), name='invite_client'),
    path('appointment_admin/', views.AppointmentAdminPageView.as_view(), name='appointment_admin'),
]
