import random
import json
import csv
import os

places = ["в лесу", "на горе", "в замке"]
weapons = ["лук", "меч", "копье", "булава", "щит"]
armors = ["Нагрудник", "Шлем", "Нагрудник + шлем"]
companions = ["Пёс", "Конь", "Пума", "Орёл"]

def save_json(hero):
    json_path = 'D:\\code piton\\saved_data.json'
    with open(json_path, 'w') as json_file:
        json.dump(hero, json_file)

def load_json():
    json_path = 'D:\\code piton\\saved_data.json'
    try:
        with open(json_path, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return None

def delete_save():
    try:
        os.remove('D:\\code piton\\saved_data.json')
        print("Сохранения удалены.")
    except FileNotFoundError:
        print("Нету сохранений.")

def update_csv(hero):
    csv_path = 'D:\\code piton\\user_data.csv'
    fieldnames = ['место сражения', 'оружие', 'броня', 'компаньон', 'история_действий']

    with open(csv_path, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:  
            writer.writeheader()

        writer.writerow(hero)

hero = {
    "место сражения": None,
    "оружие": None,
    "броня": None,
    "компаньон": None,
    "история_действий": []
}

def choose_companion():
    while True:
        print("Выберите компаньона")
        for i, companion in enumerate(companions, 1):
            print(f"{i}. {companion}")

        try:
            choice = int(input("Введите номер компаньона: "))
            if 1 <= choice <= len(companions):
                hero["компаньон"] = companions[choice - 1]
                break
            else:
                print("Выберите предложенного компаньона.")
        except ValueError:
            print("Ошибка. Выберите предложенного компаньона.")

def choose_place():
    while True:
        print("Выберите место сражения")
        for i, place in enumerate(places, 1):
            print(f"{i}. {place}")

        try:
            choice = int(input("Введите номер места событий: "))
            if 1 <= choice <= len(armors):
                hero["место сражения"] = places[choice - 1]
                break
            else:
                print("Выберите предлеженное место.")
        except ValueError:
            print("Ошибка. Выбирите предложенные предметы.")

def choose_armor():
    while True:
        print("Выберите броню для героя:")
        for i, armor in enumerate(armors, 1):
            print(f"{i}. {armor}")

        try:
            choice = int(input("Введите номер брони: "))
            if 1 <= choice <= len(armors):
                hero["броня"] = armors[choice - 1]
                break
            else:
                print("Выбирите предложенные предметы.")
        except ValueError:
            print("Ошибка. Выбирите предложенные предметы.")

def choose_weapon():
    while True:
        print("Выберите оружие для сражения с драконом:")
        for i, weapon in enumerate(weapons, 1):
            print(f"{i}. {weapon}")

        try:
            choice = int(input("Введите номер оружия: "))
            if 1 <= choice <= len(weapons):
                hero["оружие"] = weapons[choice - 1]
                break
            else:
                print("Выбирите предложенные предметы.")
        except ValueError:
            print("Ошибка. Выбирите предложенные предметы.")

def battle():
    choose_place()
    choose_armor()
    choose_weapon()
    choose_companion()
    while True:
        hero_choose = input("Герой говорит: 1.Смерть тебе чудовище, 2. Беги пока не поздно чудовище. Ваш выбор (1 или 2): ")

        if hero_choose not in ["1", "2"]:
            print("Пожалуйста, введите 1 или 2 ")
        else:
            if hero_choose == "1":
                outcome = random.choice(["Победа героя", "Проигрыш"])
            elif hero_choose == "2":
                outcome = random.choice(["Победа героя, Чудовищи не захотело уходить и проиграло.", "Проигрыш, Чудовищи не захотело уходить и победило.", ])

            print(outcome)
            hero["история_действий"].append(hero_choose)
            break

def main():
    while True:
        saved_data = load_json()
        if saved_data:
            hero.update(saved_data)
            print("Сохраненные данные.")
            print(f"Место сражения: {hero['место сражения']}")
            print(f"Броня: {hero['броня']}")
            print(f"Оружие: {hero['оружие']}")
            print(f"Компаньон: {hero['компаньон']}")
        else:
            battle()
            save_json(hero)
            update_csv(hero)
        
        replay = input("Хотите ещё раз сыграть? (да/нет) или удалить сохранение (удалить): ")
        if replay.lower() == "удалить":
            delete_save()
        if replay.lower() != "да" and replay.lower() != "удалить":
            break

if __name__ == "__main__":
    main()