# Напишите функцию, которая принимает список, 
# выбирает из него все элементы с четным индексом и возвращает их 
# в виде списка.
a = [1,2,5,8,9]
for elem in a:
     if elem % 2 == 0:
         print(elem)
    
    
list = [1,2,3,4,5,6,7,8,9]
def new(a):
    b = []
    for index in a:
        if index % 2 == 0 and index != 0:
            b.append(a[index])
    return b
print(new(list))
