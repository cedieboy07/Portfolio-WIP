import time
import runpy
import sys
import json


def _learntskills():

    def _print(string):
        sys.stdout.write(string)
        sys.stdout.flush()

    print("-" * 80)
    _print("CHAPTER 1: ")
    time.sleep(1.5)
    print("My Learnt Skills")
    time.sleep(1.5)
    print("-" * 80)

    from db_folder.skills import show_skills_menu

    show_skills_menu()

    print("-" * 80)
    print("<<--Cover Page" " | " "<--About the Author" " | " "Chapter 2-->")
    print("-" * 80)

    from cover_page import main_select
    from auth_info import _auth
    from cover_page import menu

    user_chap = input("(<<, <, or >): ")

    if user_chap == "<<":
        print("-" * 80)
        print(menu("x--End Program" " | " "About the Author-->" " | " "Chapter 1-->>"))
        main_select()
    elif user_chap == "<":
        _auth()
    elif user_chap == ">":
        runpy.run_path("chap_2.py")
