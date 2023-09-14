while True:
    try:
        digit = int(input("Введите число : "))
        if digit > 0:
            print("Все делители числа :")
            for i in range(1, digit + 1):
                if digit % i == 0:
                    print(i)
            break
        else:
            print("Число равно нулю!")
    except:
        print("Некорректный ввод!")