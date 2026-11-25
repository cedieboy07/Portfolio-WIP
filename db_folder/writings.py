import json
import sys
from pathlib import Path
from assets.terminal_ui import entry, heading, menu


def load_writings(file_path=None):
    try:
        if file_path is None:
            base_path = Path(
                getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[1])
            )
            file_path = base_path / "db_folder" / "writings.json"
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Database not found.")
        return {"written_works": []}


writing_items = [
    ("1", "Journalism"),
    ("2", "Academic writings"),
    ("3", "Creative writings"),
    ("x", "Return to chapter selection"),
]


def display_writings_by_category(writings, target_category):
    heading(target_category, "CHAPTER II / CATALOG")
    filtered = [
        item
        for item in writings.get("written_works", [])
        if item.get("category") == target_category
    ]
    for item in filtered:
        entry(
            item["title"],
            [
                ("Description", item["description"]),
                ("Link", item.get("URL", "N/A")),
            ],
        )


def show_writings_menu():
    writings = load_writings()

    while True:
        user_choice = menu(
            "Writings Index",
            writing_items,
            "Choose a category, or X to return to chapter selection:",
        )

        if user_choice == "1":
            display_writings_by_category(writings, "Journalism")
        elif user_choice == "2":
            display_writings_by_category(writings, "Academic Writing")
        elif user_choice == "3":
            display_writings_by_category(writings, "Creative Writing")
        elif user_choice == "x":
            print("Returning to chapter selection...")
            break
        else:
            print("Invalid choice. Please type '1', '2', '3', or 'x'.")


if __name__ == "__main__":
    show_writings_menu()
