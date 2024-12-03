import phonenumbers
import opencage
import folium

from test import numbers

from phonenumbers import geocoder
ch_number = phonenumbers.parse(numbers)
location = geocoder.description_for_number(ch_number, "en")
print(location)

from phonenumbers import carrier
service_nu = phonenumbers.parse(numbers)
print(carrier.name_for_number(service_nu, "en"))

from opencage.geocoder import OpenCageGeocode
key = '0cbb7ed45bc44991ba76d036ff3c5fa0'

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("c:/Desktop/Scripts/mylocation.html")