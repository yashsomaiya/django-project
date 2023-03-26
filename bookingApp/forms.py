from django import forms
from .models import WeddingBooking
class BookingForm (forms.ModelForm):
    class Meta:
        model = WeddingBooking
        fields = ['name','email','phone','location']
