import datetime

def fun():
    f = open("guvi.txt", "w")
    print(f.name)
    if f.name == "guvi.txt":
        x = datetime.datetime.now()
        f.write(f'Current date and time: " + {x}')
        f.close()  # Don't forget to close the file after writing
        print("Current date and time written to the file.")
    else:
        print("Error")

fun()

"""
Shape	Area	Perimeter
Circle	A = π × r2	Circumference = 2πr"""

# OOPS CONCEPT
"""
Create a python program called circle with constructor which will take a list an argument
From the given list create two class methods area and perimeter which will belong to calculate area and perimeter

class Circle:
    pi = 3.141

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = Circle.pi * radius * radius
        return area

    def perimeter(self):
        circumference = 2 * Circle.pi * self.radius
        return circumference


list = [10, 501, 22, 37, 100, 999, 87, 351]
for radius in list:
    circle_obj = Circle(radius)
    print(f"Radius: {radius}")
    print(f"Area: {circle_obj.area()}")
    print(f"Perimeter: {circle_obj.perimeter()}")
    
OUTPUT

Radius: 10
Area: 314.1
Perimeter: 62.82
------
Radius: 501
Area: 788394.1410000001
Perimeter: 3147.282
------
Radius: 22
Area: 1520.2440000000001
Perimeter: 138.204
------
Radius: 37
Area: 4300.0289999999995
Perimeter: 232.434
------
Radius: 100
Area: 31410.000000000004
Perimeter: 628.2
------
Radius: 999
Area: 3134721.141
Perimeter: 6275.718
------
Radius: 87
Area: 23774.229
Perimeter: 546.534
------
Radius: 351
Area: 386974.341
Perimeter: 2204.982
------ 

# TASK - 9

data =[10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x:x>4,data)
print(list)

OUTPUT
[10, 501, 22, 37, 100, 999, 87, 351]


# 2. Write a python code using lambda function to check every element of an list is integer or string

data = [10, 501, 22, 37, 100, 999, 87, 351,"KING"]
check_type = lambda x: "Integer" if isinstance(x, int) else "String"    # Check int or string using lambda function
for i in data:
    result = check_type(i)            # Check type of each element in the list
    print(f"{i} is {result}")

OUTPUT
10 is Integer
501 is Integer
22 is Integer
37 is Integer
100 is Integer
999 is Integer
87 is Integer
351 is Integer


#3 . using a python lambda function to create a fibonacci serious from 1 to 50 elements?

from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
								range(n-2), [0, 1])
print(fib(50))
"""
#OR
"""
def fibonacci(count):
   listA = [0, 1]
   any(map(lambda _:listA.append(sum(listA[-2:])),
         range(2, count)))
   return listA[:count]
print(fibonacci(50))

# 4 write a python function to validate the regular expression for following

# EMAIL ADDRESS
def is_valid_email(email):
    if email.count('@') != 1:                   # Counting '@' Symbol:
        return False
    local_part, domain_part = email.split('@')  #Splitting Local Part and Domain Part
    if not local_part or not domain_part:       #Checking Non-Empty Parts:
        return False
    domain, tld = domain_part.split('.')        #Splitting Domain and TLD(top level domain)
    if not domain or not tld:                   #Checking Non-Empty Domain and TLD
        return False
    return True
# Example usage
email1 = "user@example.com"
email2 = "invalid_email@.com"
email3 = "another.user@domain.co"
print(f"Is '{email1}' a valid email? {is_valid_email(email1)}")
print(f"Is '{email2}' a valid email? {is_valid_email(email2)}")
print(f"Is '{email3}' a valid email? {is_valid_email(email3)}")

OUTPUT
Is 'user@example.com' a valid email? True
Is 'invalid_email@.com' a valid email? False
Is 'another.user@domain.co' a valid email? True


#OR
import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' # Regular expression pattern for a valid email address
    if re.match(pattern, email): # Check if the email matches the pattern
        return True
    else:
        return False

email1 = "user@example.com"
email2 = "invalid_email@.com"

print(f"Is '{email1}'  valid - {is_valid_email(email1)}")
print(f"Is '{email2}' valid - {is_valid_email(email2)}")


OUTPUT
Is 'user@example.com'  valid - True
Is 'invalid_email@.com' valid - False

# MOBILE NUMBER OF BANGLADESH
def mobile_number(number):
    valid_number = number.replace(" ", "").replace("-", "")  # Remove spaces or dashes
    if valid_number.startswith("+880") and len(valid_number) == 14 and valid_number[4:].isdigit(): # Check if the number starts with '+880' and has 11 digits after the prefix
        return True
    if valid_number.startswith("01") and len(valid_number) == 11 and valid_number.isdigit(): # Check if the number starts with '01' and has 11 digits
        return True
    return False
# Example usage
mobile_number1 = "+8801712345678"
mobile_number2 = "01954321"
mobile_number3 = "+8801112345678"
print(f"Is '{mobile_number1}' valid - {mobile_number(mobile_number1)}")
print(f"Is '{mobile_number2}' valid -{mobile_number(mobile_number2)}")
print(f"Is '{mobile_number3}' valid - {mobile_number(mobile_number3)}")

OUTPUT
Is '+8801712345678' valid - True
Is '01954321' valid -False
Is '+8801112345678' valid - True

# TELEPHONE NUMBER OF USA
def us_phone_number(phone_number):
    valid_number = ''.join(filter(str.isdigit, phone_number)) # Remove all non-digit characters from the phone number
    if len(valid_number) == 10 and valid_number[0] in '23456789':  # Check if the cleaned number has 10 digits and starts with 2-9
        return True
    else:
        return False

# Example usage
phone_number1 = "(123) 456-7890"
phone_number2 = "555-1234"
phone_number3 = "2234567890"
print(f"Is '{phone_number1}' valid - {us_phone_number(phone_number1)}")
print(f"Is '{phone_number2}' valid - {us_phone_number(phone_number2)}")
print(f"Is '{phone_number3}' valid - {us_phone_number(phone_number3)}")

OUTPUT
Is '(123) 456-7890' valid - False
Is '555-1234' valid - False
Is '2234567890' valid - True


# Write a python fun which has 16 Characters alpha numeric password composed of alphabets of upper case , lower case , special characters , numbers.

def password(password):
    lowercase = any(char.islower() for char in password)
    uppercase = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(char in '!@#$%^&*()_+{}[]:;<>,.?~\\-/' for char in password)

    return lowercase and uppercase and digit and special_char and len(password) >= 8

password1 = "Soul@1234"
password2 = "passcode-123"

print(f"Is '{password1}' valid -  {password(password1)}")
print(f"Is '{password2}' valid - {password(password2)}")
OUTPUT
Is 'Soul@1234' valid -  True
Is 'passcode-123' valid - False


"ORR"


def is_password(password):
# Define sets of characters for different types of characters
    lowercase_charts = set('abcdefghijklmnopqrstuvwxyz')
    uppercase_charts = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    digits = set('0123456789')
    special_char = set('!@#$%^&*()_+{}\[\]:;<>,.?~\\/-')
# Initialize flags for different character types
    lowercase = False
    uppercase = False
    digit = False
    special = False
# Check each character in the password
    for char in password:
        if char in lowercase_charts:
            lowercase = True
        elif char in uppercase_charts:
            uppercase = True
        elif char in digits:
            digit = True
        elif char in special_char:
            special = True
# Check if all required character types are present and the length is at least 8 characters
    return lowercase and uppercase and digit and special and len(password) >= 8

password1 = "Hacker0001"
password2 = "crazy*Mind123"



print(f"Is '{password1}'  valid - {is_password(password1)}")
print(f"Is '{password2}'  valid - {is_password(password2)}")

OUTPUT
Is 'Hacker0001'  valid - False
Is 'crazy*Mind123'  valid - True


import random
class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.rating = 0

    def set_rating(self, rating):
        self.rating = rating


class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def calculate_average_rating(self):
        total_ratings = sum(audio.rating for audio in self.audios)
        return total_ratings / len(self.audios) if self.audios else 0


# Example usage:
playlist1 = Playlist("Playlist 1", "Pop")
playlist2 = Playlist("Playlist 2", "Rock")

audios = [Audio(f"Song {i}", f"https://example.com/song{i}.mp3") for i in range(1, 4)]
for audio in audios:
    audio.set_rating(random.randint(1, 5))

playlist1.add_audio(audios[0])
playlist1.add_audio(audios[1])
playlist2.add_audio(audios[2])

average_rating1 = playlist1.calculate_average_rating()
average_rating2 = playlist2.calculate_average_rating()

print(f"Average rating for Playlist 1: {average_rating1}")
print(f"Average rating for Playlist 2: {average_rating2}")



"""


