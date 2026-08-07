import time
import runpy
import sys

def chap_1_pages():

    def _print(string):
        sys.stdout.write(string)
        sys.stdout.flush()

    print("-" * 80)
    _print("CHAPTER 1: ")
    time.sleep(1.5)
    print("My Best Works")
    time.sleep(1.5)
    print("-" * 80)

    print("Choose a project to view")
    print("|| 1.) Project1 ||")
    print("|| 2.) Project2 ||")
    print("|| 3.) Project3 ||")

    user_page = input("(1, 2, 3, or x): ")

    if user_page == "1":
        runpy.run_path("ch1_pg1.py")
    elif user_page == "2":
        runpy.run_path("ch1_pg2.py")
    elif user_page == "3":
        runpy.run_path("ch1_pg3.py")
    elif user_page == "x":
        print("-" * 80)
        print("Choose a chapter")

    print("<<--Cover Page" " | " "<--About the Author" " | " "Chapter 2-->")

    from starting_page import main_select
    from starting_page import menu

    user_chap = input("(<<, <, or >): ")

    if user_chap == "<<":
        print("-" * 80)
        print(menu("x--End Program" " | " "About the Author-->" " | " "Chapter 1-->>"))
        main_select()
    elif user_chap == "<":
        runpy.run_path("auth_info.py")
    elif user_chap == ">":
        runpy.run_path("chap_2.py")