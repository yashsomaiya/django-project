from django import forms
from django.forms import TextInput, EmailInput, NumberInput, Textarea, DateTimeInput, DateInput
from django.utils import timezone
from .models import WeddingBooking, Service




class BookingForm (forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly': True}))
    class Meta:
        model = WeddingBooking
        fields = ['name','email','phone','location','date_booked']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Phone'
            }),
            'location': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Location'
            }),
            'date_booked': DateInput(attrs={
                'type': 'date',
                 'min': timezone.now().strftime("%Y-%m-%d")
            }),
        }


class ServicesForm (forms.ModelForm):
    class Meta:

        model = Service
        fields = ['title','service_type','header','desc','city','state','featured_package_price','organizer','image']
        labels = {'title':'Title',
                  'service_type':'Choose type of Service',
                  'header':'Provide Tags',
                  'desc':'Provide Description of your service',
                  'city':'City',
                  'state':'State',
                  'featured_package_price':'Price',
                  'organizer': 'Name of Service Provider',
                  'image': 'Upload image'
                  }
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'header': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': ''
            }),
            'desc': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 500px; height: 150px;',
                'placeholder': 'Description'
            }),
            'city': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'City'
            }),
            'state': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'state'
            }),
            'featured_package_price': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Price'
            }),
            'organizer': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Organizer'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
                'style': 'max-width: 300px;',
            })
        }


