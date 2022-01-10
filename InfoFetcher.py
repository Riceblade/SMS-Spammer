import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from phonenumbers.carrier import name_for_number
mobileno = input(
    "Enter mobile number with country code make sure to include a + at the start: ")
mobileno = phonenumbers.parse(mobileno)
ISP = carrier.name_for_valid_number(mobileno, "en")
TIMEZONE = timezone.time_zones_for_number(mobileno)
LOCATION = geocoder.description_for_number(mobileno, "en")
VALID_NUMBER_CHECK = phonenumbers.is_valid_number(mobileno)
print("===============================================")
print(mobileno)
print("Valid mobile number: ", VALID_NUMBER_CHECK)
print("Time Zone:", TIMEZONE)
print("Location:", LOCATION)
print("ISP:", ISP)
print("===============================================")
