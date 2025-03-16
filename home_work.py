from random import randint,choice

# print(randint(1, 100) )
def computer_choice():


    return randint(1, 10)



def user_choice():
    choice_ = int(input(" enter a san: "))
    return choice_


def check(c_choice, u_choice):
    if c_choice == u_choice:
        return"ugadal"
    else:
        return"ne ugadal"


def main():
    while True:
        print("1. Start")
        print("2. Exit")
        choice_ = int(input(" choosing:"))
        if choice_ == 1:
            while True:
                com_choice = computer_choice()
                us_choice = user_choice ()
                if user_choice == -1:
                    print("false choice")
                    continue
                res = check(com_choice, us_choice)
                print(res)
        elif choice_ == 2:
            break
        else:
            print("false choice")
main()







