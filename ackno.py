import time
import runpy
import sys
from assets.ascii import acknowledgements_banner
from chap_1 import _learntskills


def _acknoledgements():
    print("-" * 80)
    time.sleep(1.5)
    acknowledgements_banner()
    time.sleep(1.5)
    print("-" * 80)

    print(
        "I would like to express my sincere gratitude to my professors and mentor who have guided and will continue to guide me throughout my journey in Computer Science.\n"
        "Their expertise, patience, and encouragement have been invaluable in helping me develop my skills and knowledge in the field. I would also like to thank my friends \n"
        "and classmates who have supported me and provided valuable feedback on my projects, as well as for collaborating with me on various assignments and projects.\n"
        "Moreover, I would like to thank my family for their support, as well as for my partner for their unwavering encourangement and love. Finally, I would like to thank the\n"
        "greatest developer of all time, God, for giving me the strength and wisdom to pursue my dreams and for guiding me through the challenges of life."
    )

    time.sleep(2.5)
    print("-" * 80)
    print("x--Cover Page" " | " "<-- Final Chapter" " | " "Close Spellbook-->")

    from cover_page import main_select
    from final_chap import _bestworks
    from cover_page import menu

    user_chap = input("(x, <, or >): ")

    if user_chap == "x":
        print("-" * 80)
        print(menu("x--End Program" " | " "About the Author-->" " | " "Chapter 1-->>"))
        main_select()
    elif user_chap == "<":
        _bestworks()
    elif user_chap == ">":
        sys.exit()
