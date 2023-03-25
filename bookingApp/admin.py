from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(WeddingBooking)
admin.site.register(ContactForm)
admin.site.register(ContactNumber)
admin.site.register(Feedback)

