import time
import runpy
import sys
import json
from assets.ascii import final_chap_banner
from assets.terminal_ui import menu as terminal_menu


def _bestworks():

    time.sleep(1.5)
    final_chap_banner()
    time.sleep(1.5)

    from db_folder.flagships import show_flagships_menu

    show_flagships_menu()

    from cover_page import main_select
    from chap_3 import _createdprograms
    from ackno import _acknoledgements

    user_chap = terminal_menu(
        "Turn to a Chapter",
        [
            ("x", "Cover page"),
            ("<", "Chapter III: Created Programs"),
            (">", "Acknowledgments"),
        ],
        "Choose where to turn next:",
    )

    if user_chap == "x":
        main_select()
    elif user_chap == "<":
        _createdprograms()
    elif user_chap == ">":
        _acknoledgements()
