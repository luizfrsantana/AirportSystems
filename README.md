# Assessment#3 - AirportSystems/FlightBookingApp

## Installation

--> requirements.txt
--> Local IP: 192.168.56.104 Post: 8000

## Comands

django-admin startproject AirportSystems .
python3 manage.py runserver 192.168.56.104:8000
python3 manage.py startapp FlightBookingApp
python3 manage.py makemigrations
python3 manage.py migrate

##
JSON - Needs:
[{"key":"Content-Type","value":"application/json","description":null,"type":"text","enabled":true}]

== Flight body (raw) ==
{
  "flightNumber": "",
  "departureAirport": "",
  "arrivalAirport": "",
  "departureTime": "0000-00-00T00:00:00",
  "arrivalTime": "0000-00-00T00:00:00",
  "capacity": ,
  "price": 
}

== Passenger body (raw)==
{
  "name": "",
  "email": "",
  "phone": "",
  "address": ""
}

== Booking body (raw)==

{
  "passengerID":,
  "flightID":,
  "seat":"",
  "status":""
}