import os

def operation(number, max, min):
    while number.isdigit() == False or int(number) > max or int(number) < min:
        number = input(f'Нужно ввести только число от {min} до {max}: ')

    return number


def number(number):
    while number.isdigit() == False:
        number = input("Введи число: ")
    return number

def file_size():
    if os.stat("text.txt").st_size == 0:
        print('Список пуст!')
        return True


