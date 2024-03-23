from django.urls import path
from . import views

# URL Configurations
urlpatterns = [
    path('', views.home, name='home'),
    
    #Passenger Paths
    path('passenger_list/', views.passenger_list, name='passenger_list'), 
    path('create_passenger/', views.create_passenger, name='create_passenger'),
    path('passenger/delete/<int:passenger_id>/', views.delete_passenger, name='delete_passenger'),
    path('passenger/update/<int:passenger_id>/', views.update_passenger_form, name='update_passenger_form'), #load passenger information to update
    path('passenger/update/<int:passenger_id>/submit', views.update_passenger_submit, name='update_passenger_submit'), #submit the update
    
    #Flight Paths
    path('create_flight/', views.create_flight, name='create_flight'),
    path('flight_list/', views.flight_list, name='flight_list'), 
    path('flight/delete/<int:flight_id>/', views.delete_flight, name='delete_flight'),
    path('flight/update/<int:flight_id>/', views.update_flight_form, name='update_flight_form'), #load flight information to update
    path('flight/update/<int:flight_id>/submit', views.update_flight_submit, name='update_flight_submit'), #submit the update
    

]