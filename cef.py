def main (name, age):
    return f'hi my {name} is, i {age} years old'
print(main (12, 'dokon'))
print(main(age=12, name="Dokon"))

def main (name, age):
    return f'hi my {name} is, i {age} years old'
print(main(name="Dokon"))


'''
main(name='Dokon') - imennovannyi
main('dokon') - pozicionnyi
def main(name='Dokon') - defoltynoe znachenie , ne obyzatelnyi argument
'''

def custom_sum(*args):
    return sum(args)
print(custom_sum(2, 4, 6, 8, 9, 7,))


def print_into(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#primer use
print_into(name="Anna", age=25, city="Moskva")
print_into(width=20, height=20)


def create_profile(*hobbies, **info):
    print( f'hobbi: {hobbies}:')
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile('football', 'tennis', name='Dokon', age=20, city='Bishkek')
