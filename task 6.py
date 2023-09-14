while True:
    try:
        string = input("Введите последовательность чисел, разделённых запятой :\n")
        listOfNumbers = [int(num) for num in string.split(',') if num.isdigit()]
        break
    except ValueError:
        print("Некорректный ввод!")
tupleOfNumbers = tuple(listOfNumbers)
print("Список : ", listOfNumbers, "\nКортеж : ", tupleOfNumbers)