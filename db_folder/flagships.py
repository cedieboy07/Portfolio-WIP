import json
import sys
from pathlib import Path
from assets.terminal_ui import entry, heading, menu


def load_flagships(file_path=None):
    try:
        if file_path is None:
            base_path = Path(
                getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[1])
            )
            file_path = base_path / "db_folder" / "flagships.json"
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Database not found.")
        return {"best_works": []}


flagship_items = [
    ("1", "Programs"),
    ("2", "Writings"),
    ("3", "Films & edits"),
    ("4", "Machine designs"),
    ("x", "Return to chapter selection"),
]


def display_flagships_by_category(flagships, target_category):
    heading(target_category.strip(), "FINAL CHAPTER / CATALOG")
    filtered = [
        item
        for item in flagships.get("best_works", [])
        if item.get("category") == target_category
    ]
    for item in filtered:
        entry(item["title"], [("Description", item["description"])])


def show_flagships_menu():
    flagships = load_flagships()

    while True:
        user_choice = menu(
            "Featured Works Index",
            flagship_items,
            "Choose a category, or X to return to chapter selection:",
        )

        if user_choice == "1":
            display_flagships_by_category(flagships, "Programming ")
        elif user_choice == "2":
            display_flagships_by_category(flagships, "Writing")
        elif user_choice == "3":
            display_flagships_by_category(flagships, "Filming & Editing")
        elif user_choice == "4":
            display_flagships_by_category(flagships, "Machine Designing")
        elif user_choice == "x":
            print("Returning to chapter selection...")
            break
        else:
            print("Invalid choice. Please type '1', '2', '3', '4', or 'x'.")


if __name__ == "__main__":
    show_flagships_menu()
