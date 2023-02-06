# 1
list1 = []
# 2
list1 = ['Zeus', 'Odin', 'Hades', 'Thor', 'Seth']
# 3
print(len(list1))
# 4
print(list1[0])
print(list1[2])
print(list1[-1])
# 5
mixed_data_types = ['Thales', 25, '1,76m', 'Single', 'Jundiaí-SP']
# 6
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']
# 7
print(it_companies)
# 8
print(len(it_companies))
# 9
print(it_companies[0], it_companies[3], it_companies[-1])
# 10
it_companies[2] = 'Alibaba'
print(it_companies)
# 11
it_companies.append('Microsoft')
# 12
it_companies.insert(4, 'XXT Corporation')
# 13
it_companies[0] = it_companies[0].upper()
# 14
str = '#; '.join(it_companies)
# 15
print('IBM' in it_companies)
print('Alexa' in it_companies)
# 16
it_companies.sort()
# 17
it_companies.reverse()
# 18
print(it_companies[0:3])
# 19
print(it_companies[-3:])
# 20
print(it_companies[4:6])
