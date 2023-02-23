# my_file = open('test.txt')

# print(my_file.read())
# print(my_file.read())
# print(my_file.read())

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# print(my_file.readlines())

# my_file.close() # signals that the use of ile is over

# # This way (with) there is no need for closing the file
# with open('test.txt', mode='r') as my_file:
#     print(my_file.readlines())

# with open('test.txt', mode='a') as my_file:
#     text = my_file.write(':)')
#     print(text)

# with open('sad.txt', mode='w') as my_file:
#     text = my_file.write(':(')
#     print(text)

# File IO Erros
try:
    with open('teste.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO Error')
    raise err
