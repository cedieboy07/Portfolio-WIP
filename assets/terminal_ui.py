import re
import sys
import textwrap
import time

WIDTH = 72


def heading(title, context="THE SPELLBOOK"):
    print()
    print("=" * WIDTH)
    print(f"  {context}")
    print(f"  {title}")
    print("-" * WIDTH)


def menu(title, options, prompt="Choose an option:"):
    heading(title, "THE SPELLBOOK / INDEX")
    for key, label in options:
        print(f"  [{key.upper():>2}]  {label}")
    print()
    return input(f"  {prompt} ").strip().lower()


def paragraph(text):
    normalized_text = " ".join(text.split())
    passages = re.split(r"(?<=[.!?])\s+", normalized_text)
    narration(passages)


def narration(passages, character_delay=0.025, passage_delay=0.55):
    print()
    for passage in passages:
        lines = textwrap.wrap(passage, width=WIDTH - 4)
        for line in lines:
            print("  ", end="", flush=True)
            for character in line:
                print(character, end="", flush=True)
                if character_delay:
                    time.sleep(character_delay)
            print()
        print()
        if passage_delay:
            time.sleep(passage_delay)


def closing_message():
    narration(
        [
            "The spellbook closes, but its magic remains.",
            "Thank you for exploring these pages. Until our paths cross again.",
        ]
    )


def entry(title, details):
    print()
    print(f"  {title}")
    for label, value in details:
        if label.lower() in {"link", "url"}:
            print(f"    {label}:")
            print(f"      {value}")
            continue
        formatted = textwrap.fill(
            str(value),
            width=WIDTH - 4,
            initial_indent=f"    {label}: ",
            subsequent_indent="      ",
            break_long_words=False,
            break_on_hyphens=False,
        )
        print(formatted)
    print(f"  {'-' * (WIDTH - 4)}")
