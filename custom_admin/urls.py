from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_root'),
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='admin_dashboard'),
    path('add-flight/', views.add_flight, name='add_flight'),
    path('bookings/', views.manage_bookings, name='manage_bookings'),
    path('flights/', views.manage_flights, name='manage_flights'),
    path('flight/delete/<int:flight_id>/', views.delete_flight, name='delete_flight'),
    path('booking/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]
