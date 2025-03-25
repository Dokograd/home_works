dok  = [x for x in range(100)]
print(dok)
dok = [x for x in range(10) if x % 1== 0]
print(dok)

words = ["cat", "elephant", "dog", "giraffe"]
lengths = [len(word) for word in words]
print(lengths)

words = ["cats", "elephant", "dogs", "giraffe8"]
lengths = [len(word) for word in words]
print(lengths)

'''
[выражение for элемент in список if условие]

выражение - что делать с каждым элементом

for элемент in список - перебор элементов по отдельности

if условие - (необязательно) условие, фильтр для элементов
'''

numbers = [x for x in range(100)]
print(numbers)

numbers = []
for x in range(100):
    numbers.append(x)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

words = ['apple', 'orange', 'cherry']
short_words = [x.upper() for x in words]
print(short_words)

numbers = tuple(x for x in range(100))
print(numbers)

numbers = [x**2 for x in range(10)]
print(numbers)


rds = ["кот", "машина", "птица", "слон", "компьютер"]
filtered_words = list(filter(lambda x:len(x) % 2 == 0, words))
print(filtered_words)

