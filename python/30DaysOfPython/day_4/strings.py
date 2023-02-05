# ex1 = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
# print(ex1)
# ex2 = 'Coding ' + 'For ' + 'All '
# print(ex2)
# company = 'coding for ALL'
# print(company)
# print(len(company))
# print(company.upper())
# print(company.lower())
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())
# print(company[:6])
# print(company.find('for'))
# print(company.replace('coding', 'Python'))
str = 'Coding For All'
print('Python for Everyone'.replace('Everyone', 'All'))
print(str.split(' '))

str_big_techs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str_big_techs.split(','))

print(str[0])
print(str[-1])
print(str[10])

# str = 'Python For Everyone'
# str_arr = str.split(' ')
# for word in str_arr:
#     print(word[0], end='')
# print()

# str = 'Coding For All'
# str_arr = str.split(' ')
# for word in str_arr:
#     print(word[0], end='')
# print()

print(str.index('C'), str.index('F'), str.find('l'))
print(str.rfind('l'))
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))
print(
    'You cannot end a sentence with because because because is a conjunction'[31:54])
print(str.startswith('Coding'))
print(str.endswith('coding'))
