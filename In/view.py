import ast

def get_info():
    print('1 - посмотреть все контакты'
          "\n2 - добавить контакт"
          "\n3 - удалить контакт"
          "\n4 - поиск номер контакта по имени"
          '\n5 - завершить работу')


def get_operation():
    return input('Введи номер операции: ')

def name_user():
    return input('Введи имя контакта: ')

def number_user():
    return input('Введи номер телефона контакта: ')

def file_write(data, txt):
    with open('text.txt', txt) as file:
        if txt == 'w':
            for i in data:
                file.write(f'{i}\n')
        else:
            file.write(f'{data}\n')



def preview():

    with open('text.txt', 'r') as file:
        my_list = [row.strip() for row in file]
    for i in my_list:
        temp = ast.literal_eval(i)
        for j in temp.values():
            print(j, end = " ")
        print()


def view_number():

    with open('text.txt', 'r') as file:
        my_list = [row.strip() for row in file]
    temp2 = []
    print(my_list)
    for i in my_list:
        temp = ast.literal_eval(i)
        value = list(temp.values())
        temp2.append(value[0])

    name = input("Имя пользователя для поиска номера: ")
    while name not in temp2:
        name = input(f"Такого имени нет, выбери из {temp2}: ")
    count = 0
    print(temp2)

    for i in temp2:
         if name == i:
             temp2 = my_list[count]
         else:
             count += 1

    temp2 = ast.literal_eval(temp2)
    for i in temp2.values():
        print(i, end = " ")
    print()




