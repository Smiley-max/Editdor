import json

# Eksempel på monsterdata og sværdsdata i en JSON-fil
monsters = [
    {"name": "Obsidian Ant", "hp": 20, "dmg": (5, 10)},
    {"name": "Frost Spider", "hp": 22, "dmg": (4, 9)},
    {"name": "Rock Crusher", "hp": 55, "dmg": (5, 10)},
]

swords = [
    {"name": "Smiley Sword", "damage": 20, "special_ability": "Critical hits on rare occasions"},
    {"name": "Flame Sword", "damage": 15, "special_ability": "Burns enemies over time"},
]

# Funktion til at tilføje et monster
def add_monster(name, hp, dmg_min, dmg_max):
    new_monster = {"name": name, "hp": hp, "dmg": (dmg_min, dmg_max)}
    monsters.append(new_monster)
    print(f"{name} added to monsters!")

# Funktion til at tilføje et sværd
def add_sword(name, damage, special_ability):
    new_sword = {"name": name, "damage": damage, "special_ability": special_ability}
    swords.append(new_sword)
    print(f"{name} added to swords!")

# Funktion til at gemme ændringerne til filer
def save_changes():
    with open("monsters.json", "w") as f:
        json.dump(monsters, f, indent=4)
    with open("swords.json", "w") as f:
        json.dump(swords, f, indent=4)
    print("Changes saved to monsters.json and swords.json")

# Hovedfunktion til brugerinteraktion
def edit_elder():
    while True:
        print("\nWelcome to Editdor for Elyndor!")
        print("1. Add monster")
        print("2. Add sword")
        print("3. Save changes")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter monster name: ")
            hp = int(input("Enter monster HP: "))
            dmg_min = int(input("Enter minimum damage: "))
            dmg_max = int(input("Enter maximum damage: "))
            add_monster(name, hp, dmg_min, dmg_max)
        elif choice == "2":
            name = input("Enter sword name: ")
            damage = int(input("Enter sword damage: "))
            special_ability = input("Enter sword special ability: ")
            add_sword(name, damage, special_ability)
        elif choice == "3":
            save_changes()
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    edit_elder()
