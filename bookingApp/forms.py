from django import forms
from .models import WeddingBooking
class BookingForm (forms.ModelForm):
    class meta:
