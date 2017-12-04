# created by jenny trac
# created on dec 4 2017
# program puts a mailing address into a structure and formats it

class MailingAddress():
    def __init__(self, first_name, last_name, house_number, street_name, street_type, city_name, province, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.house_number = house_number
        self.street_name = street_name
        self.street_type = street_type
        self.city_name = city_name
        self.province = province
        self.postal_code = postal_code

# input
print("Format your mailing address:")
print("First name:")
f_name = raw_input()
print("Last name:")
l_name = raw_input()
print("House number:")
h_number = raw_input()
print("Street name:")
s_name = raw_input()
print("Street type:")
s_type = raw_input()
print("City:")
city = raw_input()
print("Province:")
prov = raw_input()
print("Postal code:")
postal = raw_input()

# process
mailing_address = MailingAddress(f_name, l_name, h_number, s_name, s_type, city, prov, postal)

# output
print(" ")
print("Your mailing address:")
print(" ")
print(str(mailing_address.first_name) + " " + str(mailing_address.last_name))
print(str(mailing_address.house_number) + " " + str(mailing_address.street_name) + " " + str(mailing_address.street_type))
print(str(mailing_address.city_name) + " " + str(mailing_address.province) + "  " + str(mailing_address.postal_code))
