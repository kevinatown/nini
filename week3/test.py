#Expon

#def power(base, exponent):  # Add your parameters here!
#  base = raw_input("Enter the base: ")
 # exponent = raw_input("Enter athe exponent: ")
  #result = base ** exponent
  #print "%d to the power of %d is %d." % (base, exponent, result)

#power(base, exponent)  # Add your arguments here!

def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!


def cube(number):
  return n = number ** number ** number

def by_three(number):
  if n % 3 == 0:
    return cube(number)
    print "n is divible by 3"
  else:
    return false
    print "n is not"


 def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False


import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!


def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  else:
    return "The city you entered does not exist"
  
def rental_car_cost(days):
  car_cost = 40 * days
  if days >= 7:
    car_cost -= 50   
  elif days >= 3 and days < 7:
    car_cost -= 20
  return car_cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
  
print trip_cost("Los Angeles", 5, 600)


numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3]

  