print("\t\tЮвелирный магазин")
catalog = {"Кольцо": ["Серебро", 49.20, 15], "Серьги": ["Золото", 367.10, 6],
           "Браслет": ["Белое золото", 695.02, 3]}
productNames = {}
mainChoice = ""
while mainChoice != "6":
    print("1. Просмотр описания : название - описание\n"
          "2. Просмотр цены : название - цена\n"
          "3. Просмотр количества : название - количество\n"
          "4. Всю информацию\n"
          "5. Покупка\n"
          "6. До свидания")
    mainChoice = input()
    if mainChoice == "1":
        for key in catalog:
            print(key, " - ", catalog[key][0])
    elif mainChoice == "2":
        for key in catalog:
            print(key, " - ", catalog[key][1], " BYN")
    elif mainChoice == "3":
        for key in catalog:
            print(key, " - ", catalog[key][2], " шт.")
    elif mainChoice == "4":
        for key in catalog:
            print(key, " - ", catalog[key][0], ", ", catalog[key][1], " BYN, ",
                  catalog[key][2], " шт.")
    elif mainChoice == "5":
        choice = ""
        while choice != "6":
            print("\t\tМеню покупки\n"
                  "1 - Добавить изделие в корзину\n"
                  "2 - Удалить изделие из корзины\n"
                  "3 - Просмотр изделий в корзине\n"
                  "4 - Посчитать общую стоимость изделий в корзине\n"
                  "5 - Оплатить\n"
                  "6 - Вернуться назад\n"
                  "7 - Выйти")
            choice = input()
            if choice == "1":
                name = input("Введите название изделия, которое вы хотите приобрести :\n")
                for key in catalog:
                    if name == catalog[key]:
                        productNames[key] = catalog[key]
                        break
                if len(productNames) == 0:
                    print("Такого изделия нет!")
                    continue
                try:
                    amount = int(input("Введите количество изделий, которое вы хотите приобрести :\n"))
                    for key in catalog:
                        if catalog[key][2] <= amount:
                            catalog[key][2] -= amount
                            productNames[key][2] = amount
                            break
                except Exception:
                    print("Некорректный ввод!")
            elif choice == "2":
                check = False
                name = input("Введите название изделия, которое вы хотите удалить :\n")
                for i in range(1, len(productNames)):
                    if name == productNames[i - 1]:
                        del productNames[i - 1]
                        check = True
                        break
                if not check:
                    print("Такого изделия нет в корзине!")
            elif choice == "3":
                for key in productNames:
                    print(key, " - ", productNames[key][0], ", ", productNames[key][1], " BYN, ",
                          productNames[key][2], " шт.")
            elif choice == "4":
                totalPrice = 0.0
                for key in productNames:
                    totalPrice += productNames[key][1] * productNames[key][2]
                print(totalPrice)
            elif choice == "5":
                print("{:.>{}}".format("", 30))
                for key in productNames:
                    print("{:.<{}}".format((key, " * ", productNames[key][2]), 20), "{:.>{}}".format((productNames[key][1], " BYN")), 10)
                if totalPrice == 0:
                    for key in productNames:
                        totalPrice += productNames[key][1] * productNames[key][2]
                print("{:.>{}}".format((totalPrice, " BYN")), 30)
                print("{:.>{}}".format("", 30))
                productNames.clear()
            elif choice == "7":
                mainChoice = "6"
                choice = "6"
    else:
        print("Такого варианта выбора нет!")
        continue