# -*- coding: utf-8 -*-
def add_country_info(countries):
    country_name = input("Введіть назву країни: ")
    part_of_world = input("Введіть частину світу, де розташована країна: ")
    area = float(input("Введіть площу країни: "))
    population = int(input("Введіть населення країни: "))

    country_info = {
        "частина_світу": part_of_world,
        "площа": area,
        "населення": population
    }

    countries[country_name] = country_info
    print(f"Інформацію про країну {country_name} додано до словника.")

# Створимо порожній словник для зберігання інформації про країни
countries = {}

# Запитаємо користувача, скільки країн він хоче додати до словника
num_countries = int(input("Скільки країн ви хочете додати до словника? "))

# Додаємо інформацію про країни за допомогою функції, стільки разів, скільки вказав користувач
for i in range(num_countries):
    add_country_info(countries)

# Шукаємо країни, які знаходяться в Африці або Азії
africa_or_asia_countries = []

for country, info in countries.items():
    part_of_world = info.get("частина_світу")
    if part_of_world == "Африка" or part_of_world == "Азія":
        africa_or_asia_countries.append(country)

# Виводимо знайдені країни
if africa_or_asia_countries:
    print("Країни, які знаходяться в Африці або Азії:")
    for country in africa_or_asia_countries:
        print(country)
else:
    print("У заданих країнах немає країн, що знаходяться в Африці або Азії.")
