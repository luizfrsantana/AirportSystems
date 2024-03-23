from django.db import models

class Passenger(models.Model):
    passengerID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    def serialize(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone' : self.phone,
            'address': self.address
        }

class Flight(models.Model):
    flightID = models.AutoField(primary_key=True)
    flightNumber = models.CharField(max_length=20)
    departureAirport = models.CharField(max_length=3)
    arrivalAirport = models.CharField(max_length=3)
    departureTime = models.DateTimeField()
    arrivalTime = models.DateTimeField()
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.flightNumber  
    
    def serialize(self):
        return {
             'FlightNumber': self.flightNumber,
              'DepartureAirport': self.departureAirport,
              'ArrivalAirport ':  self.arrivalAirport,
              'DepartureTime': self.departureTime,
              'ArrivalTime': self.arrivalTime,
              'Capacity': self.capacity, 
              'Price': str(self.price) 
        }  
    
class Booking(models.Model):
    bookingID = models.AutoField(primary_key=True)
    passengerID = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flightID = models.ForeignKey(Flight, on_delete=models.CASCADE)
    bookingDate = models.DateTimeField(auto_now_add=True)
    seatNumber = models.CharField(max_length=10)
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"BookingID: {self.bookingID}, Passenger: {self.passengerID.name}, Flight: {self.flightID.flightNumber}"
    
    def serialize(self):
        return {
              'passengerID': self.passengerID,
              'flightID ':  self.flightID,
              'bookingDate': self.bookingDate,
              'seatNumber': self.seatNumber,
              'status': self.status 
        } 