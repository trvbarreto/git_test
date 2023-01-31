# my_age = 25
# my_height = 1.76
# complex = 1j

# t_base = input('Enter the triangle base: ')
# t_height = input('Enter the triangle height: ')
# area = 0.5 * (float(t_base) * float(t_height))
# print(f'The area is {area}')

# side_a = int(input('Enter side a: '))
# side_b = int(input('Enter side b: '))
# side_c = int(input('Enter side c: '))
# perimeter = side_a + side_b + side_c
# print(f'The perimeter is {perimeter}')

# import math
# t_length = int(input('Enter the length: '))
# t_width = int(input('Enter the width: '))
# area = t_length * t_width
# perimeter = 2 * (t_length + t_width)

# circle_radius = int(input('Enter the radius: '))
# area = math.pi * (circle_radius * circle_radius)
# c_perimeter = 2 * (math.pi * circle_radius)

# script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# hours = int(input('Enter hours: '))
# rate_per_hour = int(input('Enter rate per hour: '))
# weekly_earnings = hours * rate_per_hour
# print(f'Your weekly earning is {weekly_earnings}')

#  a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# years_lived = int(input('Enter number of years you have lived: '))
# seconds_lived = ((years_lived * 365) * 24) * 3600
# print(f'You have lived for {seconds_lived} seconds')

for x in range(5):
    x += 1
    print(x, end=' ')
    for y in range(4):
        y += 1
        if (y == 1):
            print(1, end=' ')
        elif (x == 1):
            print(1, end=' ')
        else:
            y -= 1
            print(x**y, end=' ')
    print('')
