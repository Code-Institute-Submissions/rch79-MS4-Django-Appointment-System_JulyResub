from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('appointments', views.AppointmentListView.as_view(), name='appointments')
]
