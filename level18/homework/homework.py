def multiply_numbers(a, b):
    print(a * b)


multiply_numbers(5, 3)


def is_even_or_odd(number):
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტი"


print(is_even_or_odd(4))
print(is_even_or_odd(7))



def greet(name):
    print(f"Hello {name}")


greet("Giorgi")
greet("Nino")


def concatenate_strings(str1, str2):
    return str1 + str2


result = concatenate_strings("Hello, ", "world!")
print(result)
