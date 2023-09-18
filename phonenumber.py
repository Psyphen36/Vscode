import phonenumbers as pn
from phonenumbers import timezone,geocoder,carrier
number = input('Enter your number using(+__): ')

phone = pn.parse(number)
zone = timezone.time_zones_for_number(phone)
goelocation = geocoder.description_for_number(phone,'en')
carr = carrier.name_for_number(phone,'en') 

print(f'{phone}\n{zone}\n{goelocation}\n{carr}')


