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
# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_lists = front_end + back_end
print(joined_lists)
# 27
full_stack = joined_lists.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index+1, 'SQL')
full_stack.insert(redux_index+1, 'Python')
print(full_stack)
