#Import modules and files
import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_message as cust
import locale
#set a list of possible destination
destinations =['Augusta', 'Atlanta', 'Chicago', 'New York City', 'Los Angeles', 'Dallas', 'Miami', 'Wakanda']
#set current date and time
date = dt.date.today()
time = dt.datetime.now()
#format date and time to readable
formatted_date = dt.datetime.strftime(dt.date.today(), '%b %d, %Y')
formatted_time = dt.datetime.strftime(dt.datetime.now(), '%I:%M:%S %p')
print("The current date is: ", formatted_date)
print("The current time is: ", formatted_time)
#Set the year and calculate difference of the destination and current year. Then multiple by 1000.00 to calculate the trip cost.
base_cost = Decimal('1000.00')
year = randint(1, 9999)
multiplier = abs(date.year - year)
unformatted_cost = base_cost * Decimal(multiplier)
# print(year)
# print(multiplier)
# print(unformatted_cost)
#format cost to USD currency
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
cost = locale.currency(unformatted_cost, grouping=True)
destination = choice(destinations)
# print(destination)
# print a formatted message using the message for custom_mesage.py
message = cust.generate_time_travel_message(year, destination, cost)
print(message)