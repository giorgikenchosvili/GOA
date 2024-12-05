
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

start = int(input("შეიყვანეთ პირველი რიცხვი: "))
end = int(input("შეიყვანეთ მეორე რიცხვი: "))

print(my_list[start:end+1]) 




my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

index = int(input("შეიყვანეთ ინდექსი (0-4): "))

print(my_list[index])






user_name = input("შეიყვანეთ თქვენი სახელი: ")

my_name = "გიორგი"

result = user_name[:3] + my_name[-2:]
print(result)


# Indexing არის სიის ან სტრიქონის ელემენტის არჩევა მისი ინდექსის მიხედვით
# მაგალითად: my_list[2] - აირჩევა სიის მესამე ელემენტი, რადგან ინდექსირება იწყება 0-დან.
# Slicing კი ნიშნავს სიის ნაწილის აღებას, რომლისთვისაც შესაძლებელია მარცხენა და მარჯვენა საზღვრების მითითება:
# მაგალითად: my_list[1:4] - აირჩევა სიის ელემენტები ინდექსებით 1-დან 3-მდე (4 არ შედის).


last_name = input("შეიყვანეთ თქვენი გვარი: ")

reversed_last_name = last_name[::-1]

print("თქვენი გვარი:", last_name)
print("თქვენი გვარი შებრუნებულად:", reversed_last_name)
