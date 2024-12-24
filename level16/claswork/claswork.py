name = input("შეიყვანეთ თქვენი სახელი: ")
action = input("როგორ გსურთ სახელის ფორმატის შეცვლა? (lower/upper/capitalize): ").lower()

if action == "upper":
    print(name.upper())
elif action == "lower":
    print(name.lower())
elif action == "capitalize":
    print(name.capitalize())
else:
    print("არასწორი არჩევანი.")




surname = input("შეიყვანეთ თქვენი გვარი: ")

if "shvili" in surname:
    print("როგორ ხარ?")
elif "ia" in surname:
    print("მუჭო რექ?")
else:
    print("Bye")


names = ["Anna", "Mariam", "Luka", "Sandro", "Nino"]
name = input("შეიყვანეთ სახელი: ")

if name.startswith("d") and name.endswith("i"):
    names.append(name)
else:
    print("invalid")

print(names)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = int(input("შეიყვანეთ ინდექსი (0-9): "))

if 0 <= index < len(my_list):
    my_list.pop(index)
else:
    print("არასწორი ინდექსი.")

print(my_list)


food_list = ["Pizza", "Burger", "Pasta", "Sushi", "Salad"]
index = int(input("შეიყვანეთ ინდექსი (0-4): "))
favorite_food = input("შეიყვანეთ თქვენი საყვარელი საჭმელი: ")

if 0 <= index <= len(food_list):
    food_list.insert(index, favorite_food)
else:
    print("არასწორი ინდექსი.")

print(food_list)
