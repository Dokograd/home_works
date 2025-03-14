res = [i for  i in range(1,int(input())+1) if i % 2 == 0]
print(res)

n = int(input())
res = [i ** 2 for i in range (1,11)]
print(res)


print([int (i) for i in input().split(",") if int (i) > 7])

words = ["яблоко", "банан", "вишня"]
print([i.upper() for i in words])

print(["on" if int(input()) > 0 else "tak"])