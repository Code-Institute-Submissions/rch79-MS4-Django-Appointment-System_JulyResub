from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('appointments/', views.list_appointments, name='appointments'),
    path('contact_us/', views.MessageView.as_view(), name='contact_us'),
    path('test/', views.TestView.as_view(), name='test'),
    path('booking/', views.AppointmentBookingView.as_view(), name='appointment_booking'),
]
