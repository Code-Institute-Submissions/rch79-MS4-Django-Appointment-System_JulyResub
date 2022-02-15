from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('appointments', views.AppointmentListView.as_view(), name='appointments'),
    path('contact_us', views.MessageView.as_view(), name='contact_us'),
    path('booking', views.AppointmentBookingView.as_view(), name='appointment_booking'),
    path('sign_out', views.SignOut.as_view(), name='sign_out'),
    path('sign_in', views.SignIn.as_view(), name='sign_in')
]
