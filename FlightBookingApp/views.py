from django.shortcuts import render, redirect
from django.http import HttpResponse
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
        if request.body: 
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

# ========= Flight VIEWs ================

def formatted_flight(flight):
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
    if request.method == 'POST': # POST Data
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

def update_flight(request, flight_id):
    flight = formatted_flight(Flight.objects.get(flightID=flight_id))
    return render(request, 'update_flight.html', {'flight': flight})

def update_flight_by_id(request, flight_id):
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
        flight = Flight.objects.get(flightID=flight_id)
    flight.save()
    return redirect('flight_list')