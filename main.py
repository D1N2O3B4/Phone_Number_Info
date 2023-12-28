from phonenumbers import parse, geocoder, carrier, timezone

number = input("Input number here. You need to add country code to the number:")

obj = parse(number, None)
print(obj)

print(geocoder.description_for_number(obj,"en"))

print("Phone Carrier")
print(carrier.name_for_number(obj,"en"))

print("Timezone")
print(timezone.time_zones_for_number(obj))