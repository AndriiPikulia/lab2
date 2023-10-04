try:
    sum = float(input("Введіть суму депозиту:"))
    if(sum <= 0):
            print("Сума депозиту не може бути від'ємною!")
            exit()
    ypercent = float(input("Введіть значення річних відсотків:"))
    if(ypercent <= 0):
        print("Відсоток не може бути від'ємний")
        exit()
    duration = int(input("Введіть тривалість депозиту(у місяцях):"))
    if(duration <= 0):
        print("Тривалість депозиту не може бути від'ємною")
        exit()

    mpercent = ypercent / 12 / 100
    profit = sum

    for m in range(1, duration +1):
        mprofit = profit * mpercent
        profit += mprofit
        print(f"Місяць {m}, Загальна сума депозиту: {profit:.2f}, Відсотки за місяць: {mprofit:.2f}")

except ValueError:
    print("Помилкові дані!")