# 1. შექმენით სია და ამოიღეთ პირველი და ბოლო დღეები
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# ამოიღეთ პირველი და ბოლო დღე
first_day = week_days[0]
last_day = week_days[-1]

# დაბეჭდეთ შედეგი
print("First day:", first_day)
print("Last day:", last_day)

# შეცვალეთ მესამე ელემენტი "Midweek"-ით
week_days[2] = "Midweek"

# დაბეჭდეთ განახლებული სია
print("Updated list:", week_days)

# task2

# 2. მომხმარებელს სთხოვეთ საყვარელი ცხოველების სახელები
favorite_animals = []

for i in range(5):
    animal = input(f"Enter the name of your favorite animal {i+1}: ")
    favorite_animals.append(animal)

# დაბეჭდეთ პირველი და ბოლო ცხოველის სახელი
first_animal = favorite_animals[0]
last_animal = favorite_animals[-1]
print(f"First animal: {first_animal}")
print(f"Last animal: {last_animal}")

# შეცვალეთ მეორე ცხოველის სახელი
new_animal = input("Enter a new name for the second animal: ")
favorite_animals[1] = new_animal

# დაბეჭდეთ განახლებული სია
print("Updated list of favorite animals:", favorite_animals)


# task3

# 3. შექმენით სია
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# ამოიღეთ ყოველი მესამე ელემენტი
every_third = numbers[::3]
print("Every third element:", every_third)

# ამოიღეთ სია უკუღმა
numbers_reversed = numbers[::-1]
print("Reversed list:", numbers_reversed)

# სიის შუა 6 ელემენტი გადაიტანეთ ახალ სიაში
middle_six = numbers[3:9]
print("Middle six elements:", middle_six)

#task4

# 4. შექმენით სია, რომელიც შეიცავს ყველა რიცხვს 1000-დან 10000-მდე, რომლებიც იყოფა 500-ზე
numbers_divisible_by_500 = [i for i in range(1000, 10001) if i % 500 == 0]

# ამოიღეთ პირველი ხუთი რიცხვი
first_five = numbers_divisible_by_500[:5]
print("First five numbers:", first_five)

# ყოველი მესამე რიცხვი
every_third = numbers_divisible_by_500[::3]
print("Every third number:", every_third)

# დაითვალეთ ელემენტების რაოდენობა
count = len(numbers_divisible_by_500)
print("Total number of elements:", count)


# task5

# 5. მომხმარებელს სთხოვეთ 10 რიცხვის შეყვანა
numbers = input("Enter 10 numbers separated by spaces: ").split()

# გარდაქმნა რიცხვებში
numbers = [int(num) for num in numbers]

# ამოიღეთ პირველი სამი რიცხვი
first_three = numbers[:3]
print("First three numbers:", first_three)

# სიის შუა ოთხი ელემენტი
middle_four = numbers[3:7]
print("Middle four elements:", middle_four)

# შეამოწმეთ, თუ ბოლო ელემენტი არის ციფრი 10
if numbers[-1] == 10:
    print("The last number is 10.")
else:
    print("The last number is not 10.")
