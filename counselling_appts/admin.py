from django.contrib import admin
from .models import Appointment, Message

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'client', 'comment')
    list_filter = ('date', 'client')
    actions = ['confirm_appointment', 'cancel_appointment', 'set_to_pending_confirmation']

    def confirm_appointment(self, request, queryset):
        queryset.update(status = 1)

    def cancel_appointment(self, request, queryset):
        queryset.update(status = 2)

    def set_to_pending_confirmation(self, request, queryset):
        queryset.update(status = 0)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('date', 'client', 'status')
    list_filter = ('client', 'status')
    actions = ['mark_as_read', 'mark_as_unread', 'mark_as_replied']

    def mark_as_unread(self, request, queryset):
        queryset.update(status = 0)

    def mark_as_read(self, request, queryset):
        queryset.update(status = 1)

    def mark_as_replied(self, request, queryset):
        queryset.update(status = 2)
