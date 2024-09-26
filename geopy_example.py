from geopy.geocoders import Nominatim

geocoder = Nominatim(user_agent='my_app')

location = geocoder.geocode('1600 Pennsylvania Avenue NW, Washington, D.C.')

print(location.latitude, location.longitude)