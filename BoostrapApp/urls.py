from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='my_home'),
    path('about/',views.about,name='my_about'),
    path('contact/',views.contact,name='my_contact'),
    path('blog/',views.blog,name='my_blog'),
    path('booking/',views.booking,name='my_booking'),
    path('price/',views.price,name='my_price'),
    path('services/',views.services,name='my_services'),
    path('single/',views.single,name='my_single'),



]