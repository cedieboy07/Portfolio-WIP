import time
import runpy
import sys
import json
from assets.ascii import chap1_banner

def _learntskills():

    print("-" * 80)
    time.sleep(1.5)
    chap1_banner()
    time.sleep(1.5)
    print("-" * 80)

    from db_folder.skills import show_skills_menu

    show_skills_menu()

    print("-" * 80)
    print("<<--Cover Page" " | " "<--About the Author" " | " "Chapter 2-->")
    print("-" * 80)

    from cover_page import main_select
    from auth_info import _auth
    from chap_2 import _writtenworks
    from cover_page import menu

    user_chap = input("(<<, <, or >): ")

    if user_chap == "<<":
        print("-" * 80)
        print(menu("x--End Program" " | " "About the Author-->" " | " "Chapter 1-->>"))
        main_select()
    elif user_chap == "<":
        _auth()
    elif user_chap == ">":
        _writtenworks()
