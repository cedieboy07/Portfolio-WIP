import time
import sys
from chap_1 import _learntskills
from auth_info import _auth
from assets.ascii import menu_banner

def menu(chaps):
    return f"{chaps}"


def main_select():
    print("-" * 80)
    user_chap = input("(x, >, or >>): ")

    if user_chap == "x":
        print("Thank you for coming!")
        time.sleep(1.5)
        print("Hope to see you again!")
        time.sleep(1.5)
        sys.exit()
    elif user_chap == ">":
        _auth()
    elif user_chap == ">>":
        _learntskills()


def main():
    print("-" * 80)
    print("Hello Everyone!!")
    time.sleep(2.5)
    print("Welcome to....")
    time.sleep(2.5)
    menu_banner()
    time.sleep(2.5)
    print("Fill free to browse through each chapter and view their contents")
    time.sleep(2.5)

    print("-" * 80)
    print(menu("x--End Program" " | " "About the Author-->" " | " "Chapter 1-->>"))
    main_select()


if __name__ == "__main__":
    main()
