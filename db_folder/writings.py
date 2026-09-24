import json
import sys
from pathlib import Path


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
    "1.) JOURNALISM",
    "2.) ACADEMIC WRITINGS",
    "3.) CREATIVE WRITINGS",
    "x.) CHAPTER SELECT",
]


def display_writings_by_category(writings, target_category):
    print(f"--- {target_category} ---")
    filtered = [
        item
        for item in writings.get("written_works", [])
        if item.get("category") == target_category
    ]
    for item in filtered:
        print(f"Title: {item['title']} \n Description: {item['description']}")
        print("-" * 80)


def show_writings_menu():
    writings = load_writings()

    while True:
        width = 20

        for item in writing_items:
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
