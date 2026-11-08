import time
import sys
from chap_1 import _learntskills
from auth_info import _auth
from assets.ascii import menu_banner
from assets.terminal_ui import (
    closing_message,
    heading,
    menu as terminal_menu,
    narration,
)


def menu(chaps):
    return f"{chaps}"


def main_select():
    user_chap = terminal_menu(
        "Open the Spellbook",
        [
            ("x", "Close the spellbook"),
            (">", "About the author"),
            (">>", "Chapter I: Learnt Skills"),
        ],
        "Choose a destination:",
    )

    if user_chap == "x":
        closing_message()
        sys.exit()
    elif user_chap == ">":
        _auth()
    elif user_chap == ">>":
        _learntskills()


def main():
    narration(
        [
            "There are different kinds of magic, and each one of them is studied and used by different people.",
            "Some dabble in the Elements. Others delve in Primordial Forces. While a few would seek to control Dark Powers.",
            "Needless to say, magic surrounds all of us, and encompasses all things.",
            "To the point that anyone can create their own magic.",
            "This young wizard, Charles, practices one particularly unique magic:",
            "The magic of Syntax.",
        ]
    )
    menu_banner()
    time.sleep(0.8)
    main_select()


if __name__ == "__main__":
    main()
