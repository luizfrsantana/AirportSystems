from django.shortcuts import render, redirect
from .models import Passenger, Booking, Flight
import json

# Create your views here.
# Request handler

def home(request):
    return render(request, 'home.html')

# ========= Passenger VIEWs ================

def passenger_list(request):
    passengers = Passenger.objects.all()
    return render(request, 'passenger_list.html', {'passengers': passengers})

def create_passenger(request):
    if request.method == 'POST':
        # Via JSON
        if 'application/json' in request.content_type: 
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            address = data.get('address')
        # Via WEBFORM
        else: 
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
        
        # New passenger instance 
        new_passenger = Passenger(name=name, email=email, phone=phone, address=address)
        # Save passenger data
        new_passenger.save()
        return passenger_list(request)
    else:
        return render(request, 'create_passenger.html')  # form to create passenger
    
def delete_passenger(request, passenger_id):
    passenger = Passenger.objects.get(passengerID=passenger_id)
    if request.method == 'POST' or request.method == 'DELETE':
        passenger.delete()
    return redirect('passenger_list')

def update_passenger_form(request, passenger_id):
    passenger = Passenger.objects.get(passengerID=passenger_id)
    return render(request, 'update_passenger.html', {'passenger': passenger})

def update_passenger_submit(request, passenger_id):
    passenger = Passenger.objects.get(passengerID=passenger_id)
    
    if request.method == 'POST': # Via WEBFORM
        passenger.name = request.POST.get('name')
        passenger.email = request.POST.get('email')
        passenger.phone = request.POST.get('phone')
        passenger.address = request.POST.get('address')

        
    if request.method == 'PUT': # Via JSON
        data = json.loads(request.body)
        passenger.name = data.get('name')
        passenger.email = data.get('email')
        passenger.phone = data.get('phone')
        passenger.address = data.get('address')

    passenger.save()
    return redirect('passenger_list')

# ========= Flight VIEWs ================

def formatted_flight(flight): # Created to format data to be presented on the screen.
    formatted_flight = {
        'flightID': flight.flightID,
        'flightNumber': flight.flightNumber,
        'departureAirport': flight.departureAirport,
        'arrivalAirport': flight.arrivalAirport,
        'departureTime': flight.departureTime.strftime('%Y-%m-%d %H:%M'),
        'arrivalTime': flight.arrivalTime.strftime('%Y-%m-%d %H:%M'),
        'capacity': flight.capacity,
        'price': flight.price,
    }
    return formatted_flight  

def flight_list(request):
    flights = Flight.objects.all()
    formatted_flights = []
    for flight in flights: 
        formatted_flights.append(formatted_flight(flight))
        
    return render(request, 'flight_list.html', {'flights': formatted_flights})

def create_flight(request):
    if request.method == 'POST':
        # Via JSON
        if 'application/json' in request.content_type:
            data = json.loads(request.body)
            flightNumber = data.get('flightNumber')
            departureAirport = data.get('departureAirport')
            arrivalAirport = data.get('arrivalAirport')
            departureTime = data.get('departureTime')
            arrivalTime = data.get('arrivalTime')
            capacity = data.get('capacity')
            price = data.get('price')     
        # Via WEBFORM
        else:
            flightNumber = request.POST.get('flightNumber')
            departureAirport = request.POST.get('departureAirport')
            arrivalAirport = request.POST.get('arrivalAirport')
            departureTime = request.POST.get('departureTime')
            arrivalTime = request.POST.get('arrivalTime')
            capacity = request.POST.get('capacity')
            price = request.POST.get('price')
        
        # New passenger instance 
        new_flight = Flight(flightNumber=flightNumber, departureAirport=departureAirport, arrivalAirport=arrivalAirport,
                            departureTime=departureTime, arrivalTime=arrivalTime, capacity=capacity, price=price)
        # Save passenger data
        new_flight.save()
        return flight_list(request)
    else:
        return render(request, 'create_flight.html')  # form to create flight

def delete_flight(request, flight_id):
    flight = Flight.objects.get(flightID=flight_id)
    if request.method == 'POST' or request.method == 'DELETE':
        flight.delete()
    return redirect('flight_list')

def update_flight_form(request, flight_id):
    flight = formatted_flight(Flight.objects.get(flightID=flight_id))
    return render(request, 'update_flight.html', {'flight': flight})

def update_flight_submit(request, flight_id):
    flight = Flight.objects.get(flightID=flight_id)
    
    if request.method == 'POST': # Via WEBFORM
        flight.flightNumber = request.POST.get('flightNumber')
        flight.departureAirport = request.POST.get('departureAirport')
        flight.arrivalAirport = request.POST.get('arrivalAirport')
        flight.departureTime = request.POST.get('departureTime')
        flight.arrivalTime = request.POST.get('arrivalTime')
        flight.capacity = request.POST.get('capacity')
        flight.price = request.POST.get('price')
        
    if request.method == 'PUT': # Via JSON
        data = json.loads(request.body)
        flight.flightNumber = data.get('flightNumber')
        flight.departureAirport = data.get('departureAirport')
        flight.arrivalAirport = data.get('arrivalAirport')
        flight.departureTime = data.get('departureTime')
        flight.arrivalTime = data.get('arrivalTime')
        flight.capacity = data.get('capacity')
        flight.price = data.get('price')
    flight.save()
    return redirect('flight_list')

# ========= Booking VIEWs ================

def booking_list(request):
    bookings = Booking.objects.all()
    bookings_formatted = []
    for booking in bookings:
        booking_formatted = {
            "bookingID": booking.bookingID,
            "passengerName": booking.passengerID.name,
            "flightNumber":booking.flightID.flightNumber,
            "bookingDate":booking.bookingDate,
            "seatNumber":booking.seatNumber,
            "status":booking.status.capitalize(),
        }
        bookings_formatted.append(booking_formatted)
    return render(request, 'booking_list.html', {'bookings_formatted': bookings_formatted})

def create_booking(request):
    if request.method == 'POST':
        # Via JSON
        if 'application/json' in request.content_type:
            data = json.loads(request.body)
            passengerID = data.get('passengerID')
            passenger = Passenger.objects.get(pk=passengerID)
            flightID = data.get('flightID')
            flight = Flight.objects.get(pk=flightID)
            seatNumber = data.get('seat')
            status = data.get('status') 
        # Via WEBFORM
        else:
            passengerID = request.POST.get('passengerID')
            passenger = Passenger.objects.get(pk=passengerID)
            flightID = request.POST.get('flightID')
            flight = Flight.objects.get(pk=flightID)
            seatNumber = request.POST.get('seat')
            status = request.POST.get('status')

        # New passenger instance 
        new_booking = Booking(passengerID=passenger, flightID=flight,
                              seatNumber=seatNumber, status=status)
        # Save passenger data
        new_booking.save()
        return booking_list(request)
    else:
        passengers = Passenger.objects.all()
        flights = Flight.objects.all()
        # form to create booking
        return render(request, 'create_booking.html', {'passengers': passengers, 'flights': flights})  
    
def delete_booking(request, booking_id):
    booking = Booking.objects.get(bookingID=booking_id)
    if request.method == 'POST' or request.method == 'DELETE':
        booking.delete()
    return redirect('booking_list')

def update_booking_form(request, booking_id):
    booking = Booking.objects.get(bookingID=booking_id)
    booking_formatted = {
        "bookingID": booking.bookingID,
        "passengerID": booking.passengerID.passengerID,
        "passengerName": booking.passengerID.name,
        "flightID": booking.flightID.flightID,
        "flightNumber":booking.flightID.flightNumber,
        "bookingDate":booking.bookingDate,
        "seatNumber":booking.seatNumber,
        "status":booking.status.capitalize(),
    }
    return render(request, 'update_booking.html', {'booking_formatted': booking_formatted})

def update_booking_submit(request, booking_id):
    booking = Booking.objects.get(bookingID=booking_id)
    
    if request.method == 'POST': # Via WEBFORM
        booking.passengerID = Passenger.objects.get(pk=(request.POST.get('passengerID')))
        booking.flightID = Flight.objects.get(pk=(request.POST.get('flightID')))
        booking.seatNumber = request.POST.get('seat')
        booking.status = request.POST.get('status')
        
    if request.method == 'PUT': # Via JSON
        data = json.loads(request.body)
        booking.passengerID = Passenger.objects.get(pk=(data.get('passengerID')))
        booking.flightID = Flight.objects.get(pk=(data.get('flightID')))
        booking.seatNumber = data.get('seat')
        booking.status = data.get('status') 
    
    booking.save()
    return redirect('booking_list')