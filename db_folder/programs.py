import json
import sys
from pathlib import Path


def load_programs(file_path=None):
    try:
        if file_path is None:
            base_path = Path(
                getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[1])
            )
            file_path = base_path / "db_folder" / "programs.json"
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Database not found.")
        return {"created_programs": []}


programming_items = [
    "1.) SOFTWARE PROGRAMS",
    "2.) WEB PROGRAMS",
    "3.) MOBILE APPLICATIONS",
    "x.) CHAPTER SELECT",
]


def display_programs_by_category(programs, target_category):
    print(f"--- {target_category} ---")
    filtered = [
        item
        for item in programs.get("created_programs", [])
        if item.get("category") == target_category
    ]
    for item in filtered:
        print(f"Title: {item['title']} \n Description: {item['description']} \n Status: {item['status']} \n URL: {item['URL']}")
        print("-" * 80)


def show_programs_menu():
    programs = load_programs()

    while True:
        width = 20

        for item in programming_items:
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
            display_programs_by_category(programs, "Software Program")
        elif user_choice == "2":
            display_programs_by_category(programs, "Web Program")
        elif user_choice == "3":
            display_programs_by_category(programs, "Mobile Application")
        elif user_choice == "x":
            print("Returning to chapter selection...")
            break
        else:
            print("Invalid choice. Please type '1', '2', '3', or 'x'.")


if __name__ == "__main__":
    show_programs_menu()