print("Начало программы")

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

if a > b:
    max1 = b
else:
    max1 = b 
    
print(f"Среди чисел {a} и {b} наибольшее {max1}")
      
if b > c:
    max2 = b
else:
    max2 = c
 
print(f"Среди чисел {b} и {c} наибольшее {max2}") 
    
if max1 > max2:
    print(max1)
else:
    print(max2)    
print("конец программы")        