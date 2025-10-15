
def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный номер месяца"


while True:
    try:
        month_number = int(input("Введите номер месяца (1-12): "))
        season = month_to_season(month_number)
        if season == "Неверный номер месяца":
            print("Ошибка! Введите число от 1 до 12.")
            continue
        print(f"Месяц {month_number} относится к сезону: {season}")
        break
    except ValueError:
        print("Ошибка! Введите целое число.")
