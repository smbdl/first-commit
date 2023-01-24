import re

with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
    content = file.read()

while True:
    menu = int(input('1 - Считать имена и фамилии, 2 - Считать все емайлы,'
                     ' 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход '))
    if menu == 1:
        names_list = re.findall(r'\b[A-Z][a-zA-Z\'\-\. ]+\s+[a-zA-Z\'\-\. ]+\b', content)
        with open('names.txt', 'w', encoding='utf-8') as file:
            file.write(f'{len(names_list)}' + f' {names_list}')
    if menu == 2:
        email_list = re.findall(r'\w+@\w+.\w+', content)
        with open('emails.txt', 'w', encoding='utf-8') as file:
            file.write(f'{len(email_list)}' + f' {email_list}')
    if menu == 3:
        file_list = re.findall(r'[\t\s]\w+\.\w+\b', content)
        with open('files.txt', 'w', encoding='utf-8') as file:
            file.write(f'{len(file_list)}' + f' {file_list}')
    if menu == 4:
        color_list = re.findall(r'#\w{6}', content)
        with open('colors.txt', 'w', encoding='utf-8') as file:
            file.write(f'{len(color_list)}' + f' {color_list}')
    if menu == 5:
        print('stop')
        break
