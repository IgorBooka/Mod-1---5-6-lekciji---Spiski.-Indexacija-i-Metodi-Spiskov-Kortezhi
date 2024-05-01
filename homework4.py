immutable_var = 123, 456, False, 'immune'
print(immutable_var)
# immutable_var [0] = 1500
# "immutable_var [0] = 1500" выдаст ошибку "'tuple' object does not support item assignment", т.к. кортеж не поддерживает обращение по элементам
mutable_list = [True, 400, 'Gb', 40, 4, ]
print(mutable_list)
mutable_list [0] = False
mutable_list [1] = 500
mutable_list [2] = 'Mb'
print(mutable_list)

