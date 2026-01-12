from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight, Booking, Passenger
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from datetime import datetime

def customer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'airlines/customer_login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Registration successful! Please login.")
                return redirect('customer_login')
        else:
            messages.error(request, "Passwords do not match")
            
    return render(request, 'airlines/register.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    sources = Flight.objects.values_list('source', flat=True).distinct()
    destinations = Flight.objects.values_list('destination', flat=True).distinct()
    return render(request, 'airlines/home_page.html', {
        'sources': sources, 
        'destinations': destinations
    })

def search_flights(request):
    flights = []
    sources = Flight.objects.values_list('source', flat=True).distinct()
    destinations = Flight.objects.values_list('destination', flat=True).distinct()
    
    if request.method == 'POST':
        source = request.POST.get('from')
        destination = request.POST.get('to')
        date = request.POST.get('date')
        
        flights = Flight.objects.filter(source=source, destination=destination, departure_time__date=date)
        
    return render(request, 'airlines/search_flight.html', {
        'flights': flights, 
        'sources': sources, 
        'destinations': destinations
    })

def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request, 'airlines/flightpage.html', {'flight': flight})

def booking_view(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        # Create Passenger
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        # Simple passenger creation (no dup check for simplicity)
        passenger = Passenger.objects.create(
            first_name=first_name, 
            last_name="", # Booking form has only full name field currently
            email=email,
            phone=phone,
            gender="Not Specified" 
        )
        
        # Create Booking
        booking = Booking.objects.create(
            flight=flight,
            passenger=passenger,
            status='Confirmed',
            total_price=flight.price,
            travel_class=request.POST.get('class')
        )
        
        # Create Payment (Stub)
        
        return redirect('confirmation', booking_id=booking.id)
        
    return render(request, 'airlines/booking.html', {'flight': flight})

def confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'airlines/ticket.html', {'booking': booking})
