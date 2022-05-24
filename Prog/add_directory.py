from telefon.In import view
from telefon.Correct import correct_data


def writing_file():
    name_user_str = view.name_user()
    telephone_user_number = view.number_user()
    correct_data.number(telephone_user_number)
    user_info = ({"Name": name_user_str, "Telephone Number": telephone_user_number})

    return user_info

