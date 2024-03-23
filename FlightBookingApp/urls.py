from django.urls import path
from . import views

# URL Configurations
urlpatterns = [
    path('', views.home, name='home'),
    #Passenger Paths
    path('passenger_list/', views.passenger_list, name='passenger_list'), 
    path('create_passenger/', views.create_passenger, name='create_passenger'),
    path('passenger/delete/<int:passenger_id>/', views.delete_passenger, name='delete_passenger'),
    #Flight Paths
    path('create_flight/', views.create_flight, name='create_flight'),
    path('flight_list/', views.flight_list, name='flight_list'), 
    path('flight/delete/<int:flight_id>/', views.delete_flight, name='delete_flight'),
    path('flight/update/<int:flight_id>/', views.update_flight, name='update_flight'), #load flight information to update
    path('flight/update/<int:flight_id>/submit', views.update_flight_by_id, name='update_flight_by_id'), #submit the update
    

]