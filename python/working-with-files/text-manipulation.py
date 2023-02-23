try:
    with open('./text-manipulation.txt', mode='r') as my_file:
        text = my_file.read()
        with open('./smile.txt', mode='w') as my_file2:
            my_file2.write(text + ' :)')
except FileNotFoundError as e:
    print('⚠️ CHECK YOUR FILE PATH. ⚠️')
