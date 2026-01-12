from django.shortcuts import render, redirect
from airlines.models import Flight, Booking
from django.contrib import messages
from datetime import datetime

def admin_login(request):
    if request.method == 'POST':
        # hardcoded for now or use User auth
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            # Set session
            request.session['is_admin'] = True
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'custom_admin/admin_login.html')

def dashboard(request):
    # if not request.session.get('is_admin'):
    #    return redirect('admin_login')
    return render(request, 'custom_admin/admin_dashboard_sidebar.html')

def add_flight(request):
    if request.method == 'POST':
        Flight.objects.create(
            flight_number=request.POST.get('flight_number'),
            source=request.POST.get('source'),
            destination=request.POST.get('destination'),
            departure_time=request.POST.get('departure_time'),
            arrival_time=request.POST.get('arrival_time'),
            price=request.POST.get('price'),
            airline_name=request.POST.get('airline_name'),
            status=request.POST.get('status', 'Available')
        )
        return redirect('manage_flights') # or dashboard
    return render(request, 'custom_admin/add_edit_flight.html')

def manage_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'custom_admin/manage_booking.html', {'bookings': bookings})

def manage_flights(request):
    flights = Flight.objects.all()
    return render(request, 'custom_admin/manage_flights.html', {'flights': flights})

def delete_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    flight.delete()
    return redirect('manage_flights')

def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    return redirect('manage_bookings')
