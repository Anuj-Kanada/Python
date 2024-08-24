""" Create a python program capable of greeting you with Good Morning, 
    Good Afternoon and Good Evening. 
    Your program should use time module to get the current hour. 
    Here is a sample program and documentation link for you"""

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

#ecxercise Solution
import time

# Get the current hour
current_hour = int(time.strftime('%H'))

# Determine the greeting based on the hour
if (5 <= current_hour < 12):
    greeting = "Good Morning"
elif (12 <= current_hour < 17):
    greeting = "Good Afternoon"
elif (17 <= current_hour < 22):
    greeting = "Good Evening"
else:
    greeting = "Good Night"

# Print the greeting
print(greeting)
