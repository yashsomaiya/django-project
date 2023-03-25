from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path ( '' , views.index , name = 'index' ) ,
    path ( 'service/' , views.Service , name = 'services' ) ,
    path ( 'service/<uuid:service_id>/' , views.service_detail , name = 'service_detail' ) ,
    path ( 'customer/<uuid:customer_id>/' , views.customer_detail , name = 'customer_detail' ) ,
    path ( 'book/<uuid:service_id>/' , views.book_service , name = 'book_service' ) ,
    path ( 'bookings/' , views.bookings , name = 'bookings' ) ,
    path ( 'booking/<uuid:booking_id>/' , views.booking_detail , name = 'booking_detail' ) ,
    path ( 'booking/<uuid:booking_id>/pay/' , views.pay_booking , name = 'pay_booking' ) ,
    # path('admin/', admin.site.urls),
    path('about', About.as_view(), name="about"),

    path('contact', Contact.as_view(), name="contact"),
    path('feedback', Feedbacks.as_view(), name="feedback"),

    # path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('profile', Profile.as_view(), name="profile"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
