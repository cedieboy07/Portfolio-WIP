import time
import runpy
import sys
import json
from assets.ascii import final_chap_banner

def _bestworks():

    print("-" * 80)
    time.sleep(1.5)
    final_chap_banner()
    time.sleep(1.5)
    print("-" * 80)

    from db_folder.flagships import show_flagships_menu

    show_flagships_menu()

    print("-" * 80)
    print("x--Cover Page" " | " "<--Chapter 3" " | " "Acknowledgments-->")
    print("-" * 80)

    from cover_page import main_select
    from chap_3 import _createdprograms
    from ackno import _acknoledgements
    from cover_page import menu

    user_chap = input("(x, <, or >): ")

    if user_chap == "x":
        print("-" * 80)
        print(menu("x--End Program" " | " "About the Author-->" " | " "Chapter 1-->>"))
        main_select()
    elif user_chap == "<":
        _createdprograms()
    elif user_chap == ">":
        _acknoledgements()