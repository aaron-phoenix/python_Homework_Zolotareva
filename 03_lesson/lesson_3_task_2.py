from smartphone import Smartphone

catalog = [
    Smartphone("Iphone", 16, +79802346758),
    Smartphone("Iphone", 17, +79812646359),
    Smartphone("Iphone", 18, +79192355712),
    Smartphone("Samsung", "Galaxy", +79105346850),
    Smartphone("Iphone", "SE2022", +79534872910)

]

for smartphone in catalog:
    print(f"{smartphone.phone_mark} - {smartphone.phone_model} - {smartphone.phone_number}")
