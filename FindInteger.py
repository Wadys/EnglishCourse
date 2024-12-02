# Implement a program which finds integer numbers from given List.
import os
def find_integer(list):
    return_list = []
    for num in list:
        if type(num) == int:
            return_list.append(num)
    return return_list


os.system('cls')
custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']
custom_list = find_integer(custom_list)
print(custom_list)