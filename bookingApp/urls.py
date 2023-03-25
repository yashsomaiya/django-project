from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ( '' , views.index , name = 'index' ) ,
    path ( 'service/' , views.Service , name = 'services' ) ,
    path ( 'service/<uuid:service_id>/' , views.service_detail , name = 'service_detail' ) ,
    path ( 'customer/<uuid:customer_id>/' , views.customer_detail , name = 'customer_detail' ) ,
    path ( 'book/<uuid:service_id>/' , views.book_service , name = 'book_service' ) ,
    path ( 'bookings/' , views.bookings , name = 'bookings' ) ,
    path ( 'booking/<uuid:booking_id>/' , views.booking_detail , name = 'booking_detail' ) ,
    path ( 'booking/<uuid:booking_id>/pay/' , views.pay_booking , name = 'pay_booking' ) ,
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
