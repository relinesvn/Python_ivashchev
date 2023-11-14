import json

def add_country():
    new_country = {}
    new_country["назва"] = input("Введіть назву нової країни: ")
    new_country["частина_світу"] = input("Введіть частину світу, де розташована країна: ")
    new_country["площа"] = float(input("Введіть площу країни: "))
    new_country["населення"] = int(input("Введіть населення країни: "))

    countries.append(new_country)
    print(f"Інформацію про країну {new_country['назва']} додано до переліку.")

    # Оновлюємо файл countries.json
    with open("countries.json", "w", encoding="utf-8") as file:
        json.dump(countries, file, ensure_ascii=False, indent=2)

def display_all_countries():
    print("Повний перелік країн:")
    for country in countries:
        print(country["назва"])

def display_countries_in_regions():
    regions_of_interest = ["Африка", "Азія"]
    countries_in_regions = [country for country in countries if country["частина_світу"] in regions_of_interest]

    if countries_in_regions:
        print("Країни, що знаходяться в Африці або Азії:")
        for country in countries_in_regions:
            print(f"{country['назва']} - Площа: {country['площа']}, Населення: {country['населення']}")
    else:
        print("У заданих країнах немає країн, що знаходяться в Африці або Азії.")

# Завантаження даних про країни з файлу
with open("countries.json", "r", encoding="utf-8") as file:
    countries = json.load(file)

while True:
    print("\nМеню:")
    print("1 - Додати нові країни до переліку")
    print("2 - Переглянути повний перелік країн")
    print("3 - Вивести країни, що знаходяться в Африці або Азії та вивести інформацію про них")
    print("4 - Завершити роботу програми")

    choice = input("Введіть номер бажаної дії: ")

    if choice == "1":
        add_country()
    elif choice == "2":
        display_all_countries()
    elif choice == "3":
        display_countries_in_regions()
    elif choice == "4":
        print("Роботу програми завершено.")
        break
    else:
        print("Невірний вибір. Введіть коректний номер дії.")
