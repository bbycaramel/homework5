immutable_var = (13, "mice", 1.99, True)
print ("Immutable tuple:", immutable_var)

# immutable_var[1] =  "cats"
# print (immutable_var)
'''
Да мы не сможем изменить потому что: Кортежи (тип tuple) — это неизменяемый 
тип данных в Python, который используется для хранения 
упорядоченной последовательности элементов.'''

mutable_list = ["q", "w", "e", "r", "t", "y"]
mutable_list[0] = "a"
mutable_list[1] = "s"
mutable_list[2] = 'd'
print (mutable_list)

