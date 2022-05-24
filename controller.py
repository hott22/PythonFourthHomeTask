from In import view
from telefon.Correct import correct_data
from Prog import add_directory, del_directory


def tel():
    while True:
        view.get_info()
        my_choice = view.get_operation()
        my_choice = correct_data.operation(my_choice, 4, 1)

        if int(my_choice) == 2:
            view.file_write(add_directory.writing_file(), 'a')
        elif int(my_choice) == 5:
            break
        elif int(my_choice) == 1:
            if correct_data.file_size() == True:
                continue
            view.preview()
        elif int(my_choice) == 3:
            if correct_data.file_size() == True:
                continue
            del_directory.del_file()
        elif int(my_choice) == 4:
            view.view_number()















