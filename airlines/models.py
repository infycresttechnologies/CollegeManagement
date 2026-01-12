from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    airline_name = models.CharField(max_length=100)
    total_seats = models.IntegerField(default=100)
    available_seats = models.IntegerField(default=100)
    status = models.CharField(max_length=20, default='Available', choices=[('Available', 'Available'), ('Cancelled', 'Cancelled'), ('Delayed', 'Delayed')])

    def __str__(self):
        return f"{self.flight_number}: {self.source} to {self.destination}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # Allow booking without login for now if needed, or link to User
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE) # Simplified: 1 booking = 1 passenger for now or extend
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Extra fields for class, etc.
    travel_class = models.CharField(max_length=20, choices=[('Economy', 'Economy'), ('Business', 'Business'), ('First', 'First Class')], default='Economy')

    def __str__(self):
        return f"Booking {self.id} - {self.status}"

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50) # Card, etc.
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Success')

    def __str__(self):
        return f"Payment for Booking {self.booking.id}"
