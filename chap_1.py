import time
import runpy
import sys
import json
from assets.ascii import chap1_banner
from assets.terminal_ui import menu as terminal_menu, narration


def _learntskills():
    narration(
        [
            "Every craft begins with learning its first spell.",
            "Some skills are still taking shape; others grow stronger with practice.",
            "This is the collection Charles has gathered so far.",
        ]
    )
    chap1_banner()
    time.sleep(1.5)

    from db_folder.skills import show_skills_menu

    show_skills_menu()

    from cover_page import main_select
    from auth_info import _auth
    from chap_2 import _writtenworks
    from chap_3 import _createdprograms

    user_chap = terminal_menu(
        "Turn to a Chapter",
        [
            ("<<", "Cover page"),
            ("<", "About the author"),
            (">", "Chapter II: Written Works"),
            (">>", "Chapter III: Created Programs"),
        ],
        "Choose where to turn next:",
    )

    if user_chap == "<<":
        main_select()
    elif user_chap == "<":
        _auth()
    elif user_chap == ">":
        _writtenworks()
    elif user_chap == ">>":
        _createdprograms()
