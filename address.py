# This program asks a series of questions about your address and outputs a full address.

last_name = input("Please enter your last name:")
first_name = input("Please enter your first name:")
street_number = input("Please enter your street number:")
street_name = input("Please enter your street name:")
apt_box_num = input("Please enter your apartment or box number, If not applicable hit enter: ")
city = input("Please enter your city:")
state = input("Please enter your state:")
zip_code = input("Please enter your zip code:")

address = last_name, first_name, street_number, street_name, apt_box_num, city, state, zip_code,

print (f"{address[0].title()}, {address[1].title()}")
print (f"{address[2]} {address[3].title()}")
if address[4] != '':
    print (f"{address[4].upper()}")
print (f"{address[5].title()}, {address[6].upper()} {address[7]}")
