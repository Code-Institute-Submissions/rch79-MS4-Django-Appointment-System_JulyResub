# forms.py

class AppointmentForm(forms.Form):
    date = forms.CharField(max_length=255)
    time = forms.CharField(max_length=5)