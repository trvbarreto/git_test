import math

print(f'Addition 3+4 = {3+4}')
print(f'Subtraction 3-4 = {3-4}')
print(f'Multiplication 3*4 = {3*4}')
print(f'Modulus 4%3 = {4%3}')
print(f'Division 3/4 = {3/4}')
print(f'Exponential 3**4 = {3**4}')
print(f'Floor division operator 4//3 = {4//3}')

print()

my_name = 'Thales Barreto'
my_family_name = 'Varanda Barreto'
my_country = 'Brazil'
str = 'I am enjoying 30 days of python'
print(my_name)
print(my_family_name)
print(my_country)
print(str)

print()

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(my_name))
print(type(my_family_name))
print(type(my_country))

print()

my_complex = 4j
my_boolean = True
my_list = [1, 2, 3]
my_typle = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {'one': 1, 'two': 2}
print(type(my_complex))
print(type(my_boolean))
print(type(my_list))
print(type(my_typle))
print(type(my_set))
print(type(my_dict))

print()

point_a = (2, 3)
point_b = (10, 8)
d = math.sqrt(((point_b[0]-point_a[0])**2)+((point_b[1]-point_a[1])**2))
print(d)
