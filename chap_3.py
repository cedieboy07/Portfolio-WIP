import time
import runpy
import sys
import json
from assets.ascii import chap3_banner

def _createdprograms():

    print("-" * 80)
    time.sleep(1.5)
    chap3_banner()
    time.sleep(1.5)
    print("-" * 80)

    from db_folder.programs import show_programs_menu

    show_programs_menu()

    print("-" * 80)
    print("x--Cover Page" " | " "<--Chapter 1" " | " "Chapter 3-->")
    print("-" * 80)

    from cover_page import main_select
    from chap_2 import _writtenworks
    from cover_page import menu

    user_chap = input("(x, <, or >): ")

    if user_chap == "x":
        print("-" * 80)
        print(menu("x--End Program" " | " "About the Author-->" " | " "Chapter 1-->>"))
        main_select()
    elif user_chap == "<":
        _writtenworks()
    elif user_chap == ">":
        runpy.run_path("chap_2.py")