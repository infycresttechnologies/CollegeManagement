from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_flights, name='search_flights'),
    path('booking/<int:flight_id>/', views.booking_view, name='booking'),
    path('flight/<int:flight_id>/', views.flight_detail, name='flight_detail'),
    path('confirmation/<int:booking_id>/', views.confirmation, name='confirmation'),
    path('customer-login/', views.customer_login, name='customer_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
