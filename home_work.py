"""
lambda аргумент: выражение
"""

square = lambda a, b: a + b
print(square(1, 4))

string_func = lambda a: a
print(string_func('Hello, world'))

greeting = lambda: 'Hello'
print(greeting())

# map() - примениение функции ко всем элементам списка
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * 3, numbers))
print(squared)

# filtered() - филтрация элементов списка
numbers = [10, 15, 20, 25, 30]
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered)

funch = lambda a: (len(a))
print(funch("Python"))


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * 3, numbers))
print(squared)

words = ["кот", "машина", "птица", "слон", "компьютер"]
filtered_words = list(filter(lambda x:len(x) > 5, words))
print(filtered_words)


#sorted() - sortirovka s kastomnym klychom
words = ["apple", "pine apple", "banane", "pear"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

