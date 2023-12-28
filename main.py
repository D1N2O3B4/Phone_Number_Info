from phonenumbers import parse, geocoder, carrier, timezone

number = input("Input number here. You need to add country code to the number:")

obj = parse(number, None)
print(obj)

num_description = geocoder.description_for_number(obj,"en")
print(f"Number Description: {num_description}")

carrier_name = carrier.name_for_number(obj,"en")
print(f"Phone Carrier: {carrier_name}")

number_timezone = timezone.time_zones_for_number(obj)
print(f"Timezone: {number_timezone}")