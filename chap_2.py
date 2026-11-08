import time
import runpy
import sys
import json
from assets.ascii import chap2_banner
from assets.terminal_ui import menu as terminal_menu


def _writtenworks():

    time.sleep(1.5)
    chap2_banner()
    time.sleep(1.5)

    from db_folder.writings import show_writings_menu

    show_writings_menu()

    from cover_page import main_select
    from chap_1 import _learntskills
    from chap_3 import _createdprograms

    user_chap = terminal_menu(
        "Turn to a Chapter",
        [
            ("x", "Cover page"),
            ("<", "Chapter I: Learnt Skills"),
            (">", "Chapter III: Created Programs"),
            (">>", "Final Chapter: Best Works"),
        ],
        "Choose where to turn next:",
    )

    if user_chap == "x":
        main_select()
    elif user_chap == "<":
        _learntskills()
    elif user_chap == ">":
        _createdprograms()
