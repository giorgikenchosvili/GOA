for i in range(51, 151, 2):
    print(i)



sentence = input("შეიყვანეთ წინადადება: ")

for char in sentence:
    print(char)


#
i = 500
while i <= 700:
    if i % 2 == 0:  
        print(i)
    i += 1




i = 50
while i >= 0:
    print(i)
    i -= 1



favorite_number = 7


while True:
    user_input = int(input("შეიყვანეთ რიცხვი: "))
    if user_input == favorite_number:
        print("თქვენ acerted ჩემი საყვარელი რიცხვი!")
        break
    else:
        print("ცუდი რიცხვი, სცადეთ ისევ.")
