import time
import runpy
import sys
import json
from assets.ascii import chap2_banner

def _writtenworks():

    print("-" * 80)
    time.sleep(1.5)
    chap2_banner()
    time.sleep(1.5)
    print("-" * 80)

    from db_folder.writings import show_writings_menu

    show_writings_menu()

    print("-" * 80)
    print("x--Cover Page" " | " "<--Chapter 1" " | " "Chapter 3-->")
    print("-" * 80)

    from cover_page import main_select
    from chap_1 import _learntskills
    from chap_3 import _createdprograms
    from cover_page import menu

    user_chap = input("(x, <, or >): ")

    if user_chap == "x":
        print("-" * 80)
        print(menu("x--End Program" " | " "About the Author-->" " | " "Chapter 1-->>"))
        main_select()
    elif user_chap == "<":
        _learntskills()
    elif user_chap == ">":
        _createdprograms()
