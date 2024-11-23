# True or False → True
# False or True → True
# True or True → True
# False or False → False
# დასკვნა: or ოპერატორისთვის True იქნება მაშინ, როცა ნებისმიერ operand-ში ერთი ან ორივე იქნება True.




# True and True → True
# True and False → False
# False and True → False
# False and False → False დასკვნა: and ოპერატორისთვის True იქნება მხოლოდ მაშინ, როცა ყველა operand-ი იქნება True.


# or ოპერატორი:

# True or True → True
# True or False → True
# False or True → True
# False or False → False


# and ოპერატორი:

# True and True → True
# True and False → False
# False and True → False
# False and False → False



name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))


my_name = "გიორგი"  


if age >= 18 and name == my_name:
    print(True)
else:
    print(False)
