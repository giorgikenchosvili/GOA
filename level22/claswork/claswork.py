def test(a,b):
    return  a * b

print(test(4,5))


def sentences(sentence1, sentence2):
    return sentence1 + " " +sentence2

print(sentences("name","hope"))

def even(numbers):
    return [num for num in numbers if num % 2 == 0]
 
 
# task 2
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2  
    else:
        return "Invalid operator"

def make_negative( number ):
    return -abs(number)

    
def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9