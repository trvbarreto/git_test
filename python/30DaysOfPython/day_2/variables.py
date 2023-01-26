# Day 2: 30 Days of python programming

import math
first_name = input('what is your first name ')
last_name = input('what is you last name ')
full_name = 'Thales Barreto'
country = input('what country are you from? ')
city = 'Jundiaí'
age = int(input('how old are you? '))
year = 2023
is_married = False
is_true = True
is_light_on = True
a, b, c = 1, 2, 3
print(f'{first_name} {last_name} {country} {age}')

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))
print()

print(len(first_name))
print(len(first_name) - len(last_name))
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
radius = int(input('what is the radius of the circle?'))
area_of_circle = math.pi * (radius**2)
print(f'the area is: {area_of_circle}')
circum_of_circle = 2 * (math.pi * radius)
print(f'the circum is: {circum_of_circle}')
