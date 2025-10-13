from geopy.geocoders import Nominatim

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapi")

# Coordinates
latitude = 19.27576
longitude = 73.04078

# Reverse geocoding
location = geolocator.reverse((latitude, longitude), exactly_one=True)

print("Address:", location.address)

# Generate map URL (OpenStreetMap)
osm_url = f"https://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}#map=18/{latitude}/{longitude}"
print("Map URL:", osm_url)
