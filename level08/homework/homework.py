user_favorite = int(input("შეიყვანეთ თქვენი საყვარელი რიცხვი: "))  
my_favorite = 7 


if user_favorite == my_favorite:
    print("თქვენი საყვარელი რიცხვი გავს ჩემს საყვარელ რიცხვს!")
else:
    print("თქვენი საყვარელი რიცხვი არ გავს ჩემს საყვარელ რიცხვს.")

number=int(input("შეიყვანეთ თქვენი საყვარელი რიცხვი: "))

number2=5

if number==number2:
    print("true")
elif number!=5:
    print("fales")






    print(5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5)

#    5 > 3 → True (რადგან 5 მართლაც მეტია 3-ზე)
# "name" == "name" → True (შესაძლებელია, რადგან სტრიქონი თანაბარია)
# 123 == "123" → False (რიცხვი არ არის იგივე სტრიქონთან)
# 5 >= 5 → True (5 ნამდვილად მეტია ან ტოლი 5-ს)
# გამოიტანს true



age = int(input("შეიყვანეთ თქვენი ასაკი: "))
surname = input("შეიყვანეთ თქვენი გვარი: ")

my_surname = "kenchoshvili"  

if age >= 18 or surname == my_surname:
    print("თქვენ შეგიძლიათ გქონდეთ ეს უფლება.")
else:
    print("თქვენ არ გაქვთ უფლება.")



# if/else: გამოიყენება ფიქსირებული პირობების შესამოწმებლად.
# while loop: ციკლი, რომელიც უშვებს მოქმედებას სანამ არ შესრულდება გარკვეული პირობა.
# for loop: ციკლი, რომელიც განმეორდება განსაზღვრული რაოდენობის განმავლობაში.








numbers = [int(input(f"შეიყვანეთ რიცხვი {i + 1}: ")) for i in range(5)]
average = sum(numbers) / len(numbers)

first_last_product = numbers[0] * numbers[-1]

if average < first_last_product:
    print("მათი საშუალო არითმეტიკული ნაკლებია პირველი და ბოლო რიცხვის ნამრავლზე.")
else:
    print("მათი საშუალო არითმეტიკული არ არის ნაკლები.")
