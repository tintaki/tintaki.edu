#Напишите функцию, которая принимает несколько параметров. 
# Первый параметр - словарь, второй параметр - один из ключей данного словаря. 
# Функция должна выводить значение этого ключа.

notes = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
key = int(input("Search number"))
def number(name_dict):
    note = name_dict.get(key)
    print(note)
number(notes)