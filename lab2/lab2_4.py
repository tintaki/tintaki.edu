print("Start of the program")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a == b & b == c:
#Все три числа равны
    print(3)
elif a == b ^ b == c:
# Если три числа не равны,но есть пара равных,то 2
    print(2)
else:
# иначе 0, равных чисел нет
    print(0)
print("end of the program")             