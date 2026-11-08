import pyfiglet
import sys
import time


def menu_banner():
    charles = pyfiglet.figlet_format("Charles'", font="gothic")
    spellbook = pyfiglet.figlet_format("Spellbook", font="gothic")

    charles_lines = charles.splitlines()
    spellbook_lines = spellbook.splitlines()

    for left, right in zip(charles_lines, spellbook_lines):
        print(left + "   " + right)


def auth_banner():
    line1 = pyfiglet.figlet_format("About the", font="gothic")
    line2 = pyfiglet.figlet_format("Author", font="gothic")

    line1_lines = line1.splitlines()
    line2_lines = line2.splitlines()

    for left, right in zip(line1_lines, line2_lines):
        print(left + "   " + right)


def chap1_banner():
    line1 = pyfiglet.figlet_format("My", font="gothic")
    line2 = pyfiglet.figlet_format("Learnt", font="gothic")
    line3 = pyfiglet.figlet_format("Skills", font="gothic")

    line1_lines = line1.splitlines()
    line2_lines = line2.splitlines()
    line3_lines = line3.splitlines()
    for left, middle, right in zip(line1_lines, line2_lines, line3_lines):
        print(left + "   " + middle + "   " + right)


def chap2_banner():
    line1 = pyfiglet.figlet_format("My", font="gothic")
    line2 = pyfiglet.figlet_format("Written", font="gothic")
    line3 = pyfiglet.figlet_format("Works", font="gothic")

    line1_lines = line1.splitlines()
    line2_lines = line2.splitlines()
    line3_lines = line3.splitlines()
    for left, middle, right in zip(line1_lines, line2_lines, line3_lines):
        print(left + "   " + middle + "   " + right)


def chap3_banner():
    line1 = pyfiglet.figlet_format("My", font="gothic")
    line2 = pyfiglet.figlet_format("Created", font="gothic")
    line3 = pyfiglet.figlet_format("Programs", font="gothic")

    line1_lines = line1.splitlines()
    line2_lines = line2.splitlines()
    line3_lines = line3.splitlines()
    for left, middle, right in zip(line1_lines, line2_lines, line3_lines):
        print(left + "   " + middle + "   " + right)


def final_chap_banner():
    line1 = pyfiglet.figlet_format("My", font="gothic")
    line2 = pyfiglet.figlet_format("Best", font="gothic")
    line3 = pyfiglet.figlet_format("Works", font="gothic")

    line1_lines = line1.splitlines()
    line2_lines = line2.splitlines()
    line3_lines = line3.splitlines()

    for left, middle, right in zip(line1_lines, line2_lines, line3_lines):
        print(left + "   " + middle + "   " + right)

def acknowledgements_banner():
    line1 = pyfiglet.figlet_format("Acknowled", font="gothic")
    line2 = pyfiglet.figlet_format("gements", font="gothic")

    line1_lines = line1.splitlines()
    line2_lines = line2.splitlines()

    for left, right in zip(line1_lines, line2_lines):
        print(left + right)
