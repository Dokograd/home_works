from home_work import computer_choice, user_choice, check
def main():
    while True:
        print("1. Start")
        print("2. Exit")
        choice_ = int(input(" choosing"))
        if choice_ == 1:
            while True:
                com_ch = computer_choice()
                us_ch= user_choice()
                if us_ch == -1:
                    print("false choice")
                    continue
                res = check(com_ch, us_ch)
                print(res)
        elif choice_ == 2:
            break
        else:
            print("false choice")
main()