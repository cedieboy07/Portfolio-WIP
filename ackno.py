import time
import runpy
import sys
from assets.ascii import acknowledgements_banner
from chap_1 import _learntskills
from assets.terminal_ui import (
    closing_message,
    menu as terminal_menu,
    narration,
    paragraph,
)


def _acknoledgements():
    narration(
        [
            "No one learns magic alone.",
            "Teachers, friends, and family leave something behind in every success.",
            "This page is written in gratitude.",
        ]
    )
    acknowledgements_banner()
    time.sleep(1.5)

    paragraph(
        "I would like to express my sincere gratitude to my professors and mentor who have guided and will continue to guide me throughout my journey in Computer Science.\n"
        "Their expertise, patience, and encouragement have been invaluable in helping me develop my skills and knowledge in the field. I would also like to thank my friends \n"
        "and classmates who have supported me and provided valuable feedback on my projects, as well as for collaborating with me on various assignments and projects.\n"
        "Moreover, I would like to thank my family for their support, as well as for my partner for their unwavering encourangement and love. Finally, I would like to thank the\n"
        "greatest developer of all time, God, for giving me the strength and wisdom to pursue my dreams and for guiding me through the challenges of life."
    )

    from cover_page import main_select
    from final_chap import _bestworks

    user_chap = terminal_menu(
        "Close the Volume",
        [
            ("x", "Cover page"),
            ("<", "Final Chapter: Best Works"),
            (">", "Close the spellbook"),
        ],
        "Choose where to turn next:",
    )

    if user_chap == "x":
        main_select()
    elif user_chap == "<":
        _bestworks()
    elif user_chap == ">":
        closing_message()
        sys.exit()
