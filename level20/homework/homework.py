# task1
def double_integer(i):
    return i * 2

# tak2
#   ?

# task3
from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

# task4
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# task5
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# task6
def double_char(s):
    return ''.join([char * 2 for char in s])

# task7
def remove_url_anchor(url):
    return url.split('#')[0]

# task8
def sum_cubes(n):
    return sum(i**3 for i in range(1, n+1))