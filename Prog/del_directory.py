import ast
from telefon.In import view

def del_file():

    with open('text.txt', 'r') as file:
        my_list = [row.strip() for row in file]
    temp2 = []
    for i in my_list:
        temp = ast.literal_eval(i)
        value = list(temp.values())
        temp2.append(value[0])

    name = input("Имя пользователя для удаления: ")
    while name not in temp2:
        name = input(f"Такого имени нет, выбери из {temp2}: ")
    count = 0

    for i in temp2:
        if name == i:
            my_list.pop(count)
        else:
            count += 1
    view.file_write(my_list, 'w')


