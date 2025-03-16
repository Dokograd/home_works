#return - kaitaryy
#exr1
def add(a, b):
    #a=1
    #b=2

    print( a + b)#=3
    return a + b

res = add( 1, 2)
print(res)
#exr2
def weather(celsius):
    if celsius < 0:
        return" weather is cold"
    elif 0 < celsius < 20:
        return" weather is norm"
    else:
        return" weather is warm"
print(weather(-10))

