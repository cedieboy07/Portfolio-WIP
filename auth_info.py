import time
import runpy
from assets.ascii import auth_banner


def _auth():
    print("-" * 80)
    time.sleep(1.5)
    auth_banner()
    time.sleep(1.5)
    print("-" * 80)

    print(
        "Charles Daniel Nevalga, born in 2006, has been a Computer Science student in CIIT College of Innovation and Integrated Technology for 6 terms.\n"
        "With a GPU of 3.45 and more than 3 projects in his portfolio, he has proven to be a hard-working student that is striving for a bright future.\n"
        "Though a tech major, he is known to be a member of the student organization, Obelisk, as a writer with plans of taking an executive role.\n"
        "Along with other indulgences such as, Writing, Reading, and Video-Gaming, he holds true to his goal of becoming a Software Developer and his\n"
        "dream of becoming a Novelist."
    )

    time.sleep(2.5)
    print("-" * 80)
    print("<--Cover Page" " | " "Chapter 1-->" " | " "Chapter 2-->>")

    from cover_page import main_select
    from chap_1 import _learntskills
    from chap_2 import _writtenworks
    from cover_page import menu

    user_chap = input("(<, >, or >>): ")

    if user_chap == "<":
        print("-" * 80)
        print(menu("x--End Program" " | " "About the Author-->" " | " "Chapter 1-->>"))
        main_select()
    elif user_chap == ">":
        _learntskills()
    elif user_chap == ">>":
        _writtenworks()
