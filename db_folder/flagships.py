import json
import sys
from pathlib import Path


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
    "1.) PROGRAMS",
    "2.) WRITINGS",
    "3.) EDITS",
    "x.) CHAPTER SELECT",
]


def display_flagships_by_category(flagships, target_category):
    print(f"--- {target_category} ---")
    filtered = [
        item
        for item in flagships.get("best_works", [])
        if item.get("category") == target_category
    ]
    for item in filtered:
        print(f"Title: {item['title']} \n Description: {item['description']}")
        print("-" * 80)


def show_flagships_menu():
    flagships = load_flagships()

    while True:
        width = 20

        for item in flagship_items:
            print(f"|| {item:<{width}} ||")
        print("-" * 80)

        user_choice = (
            input(
                "Choose the number of the category you wish to view, or X to go back to chapter select: "
            )
            .strip()
            .lower()
        )

        if user_choice == "1":
            display_flagships_by_category(flagships, "Programming ")
        elif user_choice == "2":
            display_flagships_by_category(flagships, "Writing")
        elif user_choice == "3":
            display_flagships_by_category(flagships, "Editing")
        elif user_choice == "x":
            print("Returning to chapter selection...")
            break
        else:
            print("Invalid choice. Please type '1', '2', '3', or 'x'.")


if __name__ == "__main__":
    show_flagships_menu()