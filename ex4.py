cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print ("There are "+str(cars)+" cars available.")
print ("There are only "+str(drivers)+" drivers available.")
print ("There will be "+str(cars_not_driven)+" empty cars today.")
print ("We can transport "+str(carpool_capacity)+" people today.")
print ("We have "+str(passengers)+" to carpool today.")
print ("We need to put about "+str(int(average_passengers_per_car))+" in each car.")


# When Zed wrote this program the first time he had a mistake, and Python told him about it like this:

'''
 Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
  NameError: name 'car_pool_capacity' is not defined
'''

# The program threw the above error for Zed because it couldn't find car_pool_capacity variable defined.

# Zed used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
## The value for carpool_capacity changes from float to integer.

# Try running python from the Terminal as a calculator like you did before and use variable names to do your calculations.
# Popular variable names are also i, x, and j.

i = 25
j = 3
x = 2
y = 5

print ("I will now count my chickens:")
# divides and adds
print ("Hens", float(i + 30 / 6))
# multiplies, mods and then subtracts
print ("Roosters", float(100 - i * j % 4))

print ("Now I will count the eggs:")
#mods,divides,adds and then subtracts
print (float(j + x + 1 - y + 4 % x - 1 / 4 + 6))

#adds, subtracts and then weighs
print ("Is it true that 3 + 2 < 5 - 7?")
print (j + x < y - 7)

print ("What is 3 + 2?", j + x)
print ("What is 5 - 7?", y - 7)

print ("Oh, that's why it's False.")

print ("How about some more.")

print ("Is it greater?", y > -x)
print ("Is it greater or equal?", y >= -x)
print ("Is it less or equal?", y <= -x)

# How can I print without spaces between words in print?
print ("Hey %s there." % "you")
