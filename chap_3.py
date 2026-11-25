import time
import runpy
import sys
import json
from assets.ascii import chap3_banner
from assets.terminal_ui import menu as terminal_menu, narration


def _createdprograms():
    narration(
        [
            "Some ideas are too restless to stay on the page.",
            "With code, they become tools, experiments, and worlds to explore.",
            "These are the programs Charles has brought to life.",
        ]
    )
    chap3_banner()
    time.sleep(1.5)

    from db_folder.programs import show_programs_menu

    show_programs_menu()

    from cover_page import main_select
    from chap_2 import _writtenworks
    from final_chap import _bestworks

    user_chap = terminal_menu(
        "Turn to a Chapter",
        [
            ("x", "Cover page"),
            ("<", "Chapter II: Written Works"),
            (">", "Final Chapter: Best Works"),
        ],
        "Choose where to turn next:",
    )

    if user_chap == "x":
        main_select()
    elif user_chap == "<":
        _writtenworks()
    elif user_chap == ">":
        _bestworks()
