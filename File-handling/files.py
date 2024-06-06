import re

#1. Create a regex that finds integers without size limit.
s = "sss9gd7ds8sfsfs"
pattern = r'\d+'
result = re.findall(pattern, s)
print(result)

#2. Create a regex that finds negative integers without size limit.
s = "sssgdds-8sfs-9fs"
pattern = r'-\d+'
result = re.findall(pattern, s)
print(result)

#3. Create a regex that finds (positive or negative) integers without size limit.
s = "sssgdds-8s8f9sfs"
pattern = r'-?\d+'
result = re.findall(pattern, s)
print(result)

#4. Capture all the numbers of the following sentence :
text = "21 scouts and 3 tanks fought against 4,003 protestors, so the manager was not 100.00% happy."
pattern = r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b'
result = re.findall(pattern, text)
print(result)

#5. Find all words that end with 'ly'. :
text = "He had prudently disguised himself but was quickly captured by the police."
pattern = r'\b\w+ly\b'
result = re.findall(pattern, text)
print(result)

#6. License plate number :

# A license plate consists of 2 capital letters, a dash ('-'), 3 digits, a dash ('-')
# and finally 2 capital letters. Write a script to check that an input string is a license plate.#
# If it's correct, print "good". If it's not correct, print "Not good".
plate = input("Enter your license plate number: ")
pattern = r'\b[A-Z]{2}-\d{3}-[A-Z]{2}\b'
result = re.match(pattern, plate)
if result is None:
    print("Not good")
else:
    print("good")

#7 . Address IPV4

# An IPv4 address is composed of 4 numbers between 0 and 255 separated by '.'
# Write a script to verify that a string entered is that of an IPv4 address.
ip = input("Enter your IP address :")
pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
result = re.match(pattern, ip)
if result is None:
    print("Not valid")
else:
    print("valid")

#8. Valid Mail

# An email is composed of alphanumeric characters followed by @ and a domain name.
# Write a script that checks that the string entered by a user is indeed that of an email,
# otherwise ask him to re-enter it again (until he gets a valid email).
mail = input("Enter a valid Mail :")
pattern = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{1,3}$'
result = re.match(pattern, mail)
if result is None:
    print("Not valid")
else:
    print("valid")

#9. Valid Password

# The password must now contain at least 6 characters AND
# at least one lowercase letter AND
# at least one uppercase letter AND
# at least one number AND
# at least one special character (among `$#@`).
password = input("Enter your password :")
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,}$'
result = re.match(pattern, password)
if result is None:
    print("Not valid")
else:
    print("valid")

