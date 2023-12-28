from phonenumbers import parse, geocoder, carrier

number = input("Input number here. You need to add country code to the number:")

obj = parse(number, None)
print(obj)

print(geocoder.description_for_number(obj,"en"))

print(carrier.name_for_number(obj,"en"))