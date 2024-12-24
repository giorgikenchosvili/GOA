# append(x): ამატებს ელემენტს (x) სიის ბოლოში.

# არგუმენტი: x - ელემენტი, რომელიც უნდა დაემატოს.
# insert(i, x): ამატებს ელემენტს (x) მოცემულ ინდექსზე (i).

# არგუმენტები: i - ინდექსი, სადაც ელემენტი უნდა დაემატოს; x - ელემენტი.
# pop(i=-1): შლის ელემენტს სიის მოცემული ინდექსიდან (i) და აბრუნებს მას. თუ არგუმენტი არ გადაეცემა, შლის ბოლო ელემენტს.

# არგუმენტი: i (არასავალდებულო) - ინდექსი.
# len(x): აბრუნებს ობიექტის (სიის, სტრინგის და ა.შ.) სიგრძეს.

# არგუმენტი: x - ობიექტი, რომლის სიგრძე უნდა გამოვთვალოთ.
# upper(): სტრინგის ყველა ასოს გარდაქმნის დიდ ასოებად.

# არგუმენტები: არ საჭიროებს.
# lower(): სტრინგის ყველა ასოს გარდაქმნის პატარა ასოებად.

# არგუმენტები: არ საჭიროებს.
# capitalize(): სტრინგის პირველ ასოს გარდაქმნის დიდ ასოდ და დანარჩენს პატარა ასოებად ტოვებს.

# არგუმენტები: არ საჭიროებს.
# find(sub): აბრუნებს სტრინგში არჩეული ქვეწერის (sub) პირველ ინდექსს ან -1-ს, თუ ქვეწერი არ მოიძებნა.

# არგუმენტი: sub - ქვეწერი, რომლის პოვნა გვინდა.



# 1
surnames = ["kenchoshvili", "shavgulidze", "sirdadze", "tavadze", "gocadze"]
name = input("შეიყვანეთ თქვენი სახელი: ")
if len(name) > 7:
    surnames.append(name)
print(surnames)



# 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_index_elements = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
print(even_index_elements)

# 3
my_string = "This is a string."
length = len(my_string)
print(f"სტრინგში არის {length} სიმბოლო.")


# 4
name = input("შეიყვანეთ თქვენი სახელი დიდი ასოებით: ")
name = name.lower()
print(name)


# 5
surname = "kenchoshvili"
surname = surname.upper()
print(surname)


# 6
string = "example"
string = string.capitalize()
print(string)
