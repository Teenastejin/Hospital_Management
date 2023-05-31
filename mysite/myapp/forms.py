from django import forms
from django.forms import ModelForm,widgets
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"
        widgets={
            'Patient_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Patient_Contact':forms.NumberInput(attrs={'class':'form-control'}),
            'Patient_Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Doctor_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Booking_Date':DateInput(attrs={'class':'form-control'}),

        }


class careerform(forms.ModelForm):
    class Meta:
        model= Career
        fields = "__all__"
        widgets={
            'f_name':forms.TextInput(attrs={'class':'form-control'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'})

        }

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Contact':forms.NumberInput(attrs={'class':'form-control'}),
            'Message':forms.TextInput(attrs={'class':'form-control'})


        }