import time
import sys
import runpy
from chap_1 import _learntskills
from auth_info import _auth

print("-" * 80)
print("Hello Everyone!!")
time.sleep(2.5)
print("Welcome to my portfolio!")
time.sleep(2.5)
print("Fill free to browse through each chapter and view their contents")
time.sleep(2.5)

print("-" * 80)


def menu(chaps):
    return f"{chaps}"


print(menu("x--End Program" " | " "About the Author-->" " | " "Chapter 1-->>"))


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

main_select()
