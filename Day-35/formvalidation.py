
'''
import re
fullname = input("enter the full name: ")
pattern = r'^[A-Za-z]{2,25}([A-Za-z]{2,25})+$'
res = re.match(pattern, fullname)
print("valid full name" if res else "invalid full name")

'''

'''
import re
email = input("enter the email: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
res = re.match(pattern, email)
print("valid email" if res else "invalid email")

'''


'''
import re
phone_number = input("enter the phone number: ")
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
res = re.match(pattern, phone_number)
print("valid phone number" if res else "invalid phone number")

'''


'''
import re
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!%?&])[A-Za-z0-9@$!%?&]{8,}$'
password = input("Enter your password: ")
res = re.fullmatch(pattern, password)
print("Valid password" if res else "Invalid password")

'''

'''
import re
password = input("Enter your aadhar number: ")
pattern = r'^\d{12}$'
res = re.fullmatch(pattern, password)
print("Valid aadhar number" if res else "Invalid aadhar number")

'''


import re
password = input("Enter your pancard number: ")
pattern = r'^[A-Z]{5}\d{4}[A-Z]{1}$'
res = re.fullmatch(pattern, password)
print("Valid pancard number" if res else "Invalid pancard number")


