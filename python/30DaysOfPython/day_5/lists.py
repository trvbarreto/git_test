# # 1
# list1 = []
# # 2
# list1 = ['Zeus', 'Odin', 'Hades', 'Thor', 'Seth']
# # 3
# print(len(list1))
# # 4
# print(list1[0])
# print(list1[2])
# print(list1[-1])
# # 5
# mixed_data_types = ['Thales', 25, '1,76m', 'Single', 'Jundiaí-SP']
# # 6
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']
# # 7
# print(it_companies)
# # 8
# print(len(it_companies))
# # 9
# print(it_companies[0], it_companies[3], it_companies[-1])
# # 10
# it_companies[2] = 'Alibaba'
# print(it_companies)
# # 11
# it_companies.append('Microsoft')
# # 12
# it_companies.insert(4, 'XXT Corporation')
# # 13
# it_companies[0] = it_companies[0].upper()
# # 14
# str = '#; '.join(it_companies)
# # 15
# print('IBM' in it_companies)
# print('Alexa' in it_companies)
# # 16
# it_companies.sort()
# # 17
# it_companies.reverse()
# # 18
# print(it_companies[0:3])
# # 19
# print(it_companies[-3:])
# # 20
# print(it_companies[4:6])
# # 21
# print(it_companies)
# it_companies.pop(0)
# print(it_companies)
# # 22
# length = len(it_companies)
# if length % 2 != 0:
#     arg = int(length/2)
#     del it_companies[arg]
# else:
#     arg = int(length/2)
#     del it_companies[arg-1:arg+1]
# print(it_companies)
# # 23
# it_companies.pop()
# print(it_companies)
# # 24
# del it_companies[0:len(it_companies)+1]
# print(it_companies)
# # 25
# del it_companies
# print(it_companies)
# # 26
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node', 'Express', 'MongoDB']
# joined_lists = front_end + back_end
# print(joined_lists)
# # 27
# full_stack = joined_lists.copy()
# redux_index = full_stack.index('Redux')
# full_stack.insert(redux_index+1, 'SQL')
# full_stack.insert(redux_index+1, 'Python')
# print(full_stack)

# # Exercise 2
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()
# print(f'The min age is {ages[0]}')
# print(f'The max age is {ages[-1]}')
# ages.append(19)
# ages.append(26)
# print(ages)
# ages.sort()
# if len(ages) % 2 != 0:
#     index = int(len(ages)/2)
#     print(f'The median age is {ages[index]}')
# else:
#     index = int(len(ages)/2)
#     print(f'The median age is {(ages[index]+ages[index-1])/2}')
# sum = 0
# for item in ages:
#     sum = sum + item
# print(f'The average age is {sum/len(ages)}')
# range_of_ages = ages[-1] - ages[0]
# print(f'The range of ages is {range_of_ages}')
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

# 1
# if len(countries) % 2 != 0:
#     index = int(len(countries)/2)
#     print(f'The middle country is {countries[index]}')
# else:
#     index = int(len(countries)/2)
#     print(
#         f'The middle countries are {countries[index]} and {countries[index-1]}')

# # 2
# if len(countries) % 2 != 0:
#     index = int(len(countries)/2)
#     print(f'The first part is {countries[0:index+1]}')
#     print(f'The second part is {countries[index+1:-1]}')
# else:
#     index = int(len(countries)/2)
#     print(f'The first part is {countries[0:index]}')
#     print(f'The second part is {countries[index:-1]}')

# # 3
# first, second, third, *scandic = ['China', 'Russia',
#                                   'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# print(f'The first country is {first}')
# print(f'The second country is {second}')
# print(f'The third country is {third}')
# print(f'The scandic countries are {scandic}')
