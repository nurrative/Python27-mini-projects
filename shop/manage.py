"CRUD"
# create-создать
# read -
# update-
# delete-

from products import create,read

while True:
    oper = input("Создать/удалить/обновить/просмотреть: ")
    if oper == 'c':
        create()
    elif oper == 'r':
        read()