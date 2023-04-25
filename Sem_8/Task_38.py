# добавляет новую строку
def add_cont():
    file = open ('файл.txt', 'a', encoding='UTF-8')
    data1 = input('Введите ФИО: ')
    data2 = input('Введите номер телефона: ')
    data3 = input('Введите комментарий: ')
    data = '\n' + data1 + '; ' + data2 + '; ' + data3 
    print(data)
    file.write(data)
    file.close()
    
# показывает справочник целиком
def read_cont():
    # file = open('файл.txt', 'r', encoding='UTF-8')
    # data = file.readlines()
    # file.close()
    # for contact in data:
    #     print(contact)
    #     read_cont()
    # file.close()
    with open('файл.txt', 'r', encoding='utf-8') as data:
        for contact in data:
            print(contact)

# поиск информации в справочнике
def find_cont():
    file = open('файл.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    find_cont = input('Введите информацию для поиска: ')
    for cont in data:
        if find_cont.lower() in cont.lower():
            print(cont)
    find_cont()  
    file.close()  

# изменяет данные
def change_cont():
    phone_book = []

    file = open('файл.txt', 'r+', encoding='UTF-8')
    data = file.readlines()
    file.close()
    i = 0
    for contact in data:
        new_contact = contact.strip().split(';')
        new_contact = {'name':new_contact[0],
                    'phone':new_contact[1],
                    'comment':new_contact[2]}
        phone_book.append(new_contact)
        i +=1
    print(phone_book)
    elem = int(input('Введите id: '))
    print(phone_book[elem])
    print('Выберете, что хотите изменить:')
    print('1 - ФИО, 2 - телефон, 3 - комментарий')
    char = input()
    if char == 1:
        inp = input('Введите значение\n')
        new_contact[0] = inp
        return char, inp
    elif char== 2:
        inp = input('Введите значение\n')
        new_contact[1] = inp
        return char, inp
    elif char== 3:
        inp = input('Введите значение\n')
        new_contact[2] = inp
        return char, inp
    else:    
        return 'q', 'q'
    file.close()

# Удаляет данные из телефонной книги    
def del_cont():
    with open('файл.txt', 'r', encoding="utf-8") as f:
        X = input('Введите Имя или Фамилию для удаления: ')
        lines = f.readlines()
        with open('файл.txt', 'w', encoding="utf-8") as f:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    f.write(line)
    file.close()

path = 'файл.txt'

try:                        
    file = open(path, 'r')  
except IOError:             
    print('Создан новый справочник -> файл.txt ')
    file = open(path, 'w')
finally:                    
    file.close()

actions = {'1': 'чтение',
           '2': 'запись',
           '3': 'поиск',
           '4': 'изменение',
           '5': 'удаление',
           'q': 'выход'
           }

action = None
while action != 'q':
    print('Какое действие вы хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
    action = input()
    if action == '1':
        read_cont()
    elif action == '2':
        add_cont()
    elif action == '3':
        find_cont()
    elif action == '4':
        change_cont()
    elif action == '5':
        del_cont()