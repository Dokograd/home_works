# try :
#     a = 3
#     b = 4
#     c = a / b
#     print(c)
# except SyntaxError:
#     print("4 tu 3 ko bolgongo bolgohgo bolboit ")
# except Exception:
#     print("kandaydyr bir kata")

# def is_date(day, month, year):
#     from datetime import date
#     try :
#         return date(year, month , day)
#     except ValueError:
#         return"kalendarda myndai data jok!"
#
# print(is_date(18,3,2025))
# print(is_date(29,2,2025))

def dok():
    try:
        numbers = [1,2,3,4,5,]
        a = int(input())
        print(numbers[a])
    except IndexError:
        print("mynday san jok")





dok()



















