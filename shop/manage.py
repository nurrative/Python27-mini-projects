"CRUD"
# create - создать
# read - читать
# update - изменить
# delete - удалить

from products import create,read,delete,update

while True:
    oper = input("c/r/u/d: ")
    if oper == 'c':
        create()
    elif oper == 'r':
        read()
    elif oper=='u':
        update()
    elif oper=='d':
        delete()
    