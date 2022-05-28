# forms.py
from django import forms
from allauth.account.forms import SignupForm

class AppointmentForm(forms.Form):
    date = forms.CharField(max_length=255)
    time = forms.CharField(max_length=5)


# class NameForm(forms.Form)
#     first_name = forms.CharField(label='First Name', max_length=50)
#     last_name = forms.CharField(label='Last Name', max_length=50)



class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user