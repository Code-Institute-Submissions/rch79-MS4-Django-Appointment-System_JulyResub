from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('appointments/', views.list_appointments, name='appointments'),
    path('confirmation/', views.display_confirmation_page, name='confirmation'),
    path('booking/', views.book_appointment, name='appointment_booking'),
    path('booking/success', views.confirm_appointment, name='success'),
]
