from random import choice


def computer_choice():
    return choice(['tash', 'kaichy', 'kagaz'])


def user_choice():
    print('1,tash')
    print('2,kaichy')
    print('3,kagaz')
    choice_ = int(input("chooce on this:"))
    if choice_ == 1:
        return "tash"
    elif choice_ == 2:
        return "kaichy"
    elif choice_ == 3:
        return "kagaz"
    else:
        return -1


def check(c_choice, u_choice):
    if c_choice == u_choice:
        return 'nichy'
    elif c_choice == " tash" and (u_choice == "kaichy"):
        print(f"Computer: {c_choice} - User: {u_choice}")
        return 'you are lose'
    elif c_choice == "kaichy" and u_choice == "kagaz":
        print(f"Computer: {c_choice} - User: {u_choice}")
        return 'you are lose'
    elif c_choice == "kagaz" and u_choice == "tash":
        print(f"Computer: {c_choice} - User: {u_choice}")

        return 'you are lose'
    else:
        print(f"Computer: {c_choice} - User: {u_choice}")
        return "YES! you are win"


