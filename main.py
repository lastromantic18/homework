#print("Введите число a=")
#a = int(input())
#if a>100:
#    print("Введите число">100)
#elif  a > 50 and a < 100:
#    print("Введенное число находится в пределах от 50 до 100")
#elif a == 100:
#    print("Введенное число = 100")
#else:
#    print("Введенное число < 50")

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first == second == third:
    print(3)
elif (first == second and first != third) or (first == third and first != second) or (second == third and second != first):
    
    print(2)
else:
    print(0)
    
    

 
 