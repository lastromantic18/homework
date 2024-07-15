def get_password(n):


    result = ""
    used_pairs = set() 
    for i in range(1, n):
        for j in range(1, n):
            if (i + j) == n and (str(i) + str(j) not in used_pairs):
                result += str(i) + str(j)
                used_pairs.add(str(i) + str(j))  
    return result


n = int(input("Введите число (от 3 до 20): "))


if 3 <= n <= 20:
    password = get_password(n)
    print(f"Пароль: {password}")
else:
    print("Неверное число. Введите число от 3 до 20.")