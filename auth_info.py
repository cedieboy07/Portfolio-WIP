import time
import runpy
from assets.ascii import auth_banner
from assets.terminal_ui import menu as terminal_menu, paragraph


def _auth():
    time.sleep(1.5)
    auth_banner()
    time.sleep(1.5)

    paragraph(
        "Charles Daniel Nevalga, born in 2006, has been a Computer Science student in CIIT College of Innovation and Integrated Technology for 6 terms.\n"
        "With a GPU of 3.45 and more than 3 projects in his portfolio, he has proven to be a hard-working student that is striving for a bright future.\n"
        "Though a tech major, he is known to be a member of the student organization, Obelisk, as a writer with plans of taking an executive role.\n"
        "Along with other indulgences such as, Writing, Reading, and Video-Gaming, he holds true to his goal of becoming a Software Developer and his\n"
        "dream of becoming a Novelist."
    )

    from cover_page import main_select
    from chap_1 import _learntskills
    from chap_2 import _writtenworks

    user_chap = terminal_menu(
        "Turn to a Chapter",
        [
            ("<", "Cover page"),
            (">", "Chapter I: Learnt Skills"),
            (">>", "Chapter II: Written Works"),
        ],
        "Choose where to turn next:",
    )

    if user_chap == "<":
        main_select()
    elif user_chap == ">":
        _learntskills()
    elif user_chap == ">>":
        _writtenworks()
