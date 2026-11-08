import json
import sys
from pathlib import Path
from assets.terminal_ui import entry, heading, menu


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
    ("1", "Software programs"),
    ("2", "Web programs"),
    ("3", "Mobile applications"),
    ("x", "Return to chapter selection"),
]


def display_programs_by_category(programs, target_category):
    heading(target_category, "CHAPTER III / CATALOG")
    filtered = [
        item
        for item in programs.get("created_programs", [])
        if item.get("category") == target_category
    ]
    for item in filtered:
        entry(
            item["title"],
            [
                ("Description", item["description"]),
                ("Status", item["status"]),
                ("Link", item.get("URL", "N/A")),
            ],
        )


def show_programs_menu():
    programs = load_programs()

    while True:
        user_choice = menu(
            "Programs Index",
            programming_items,
            "Choose a category, or X to return to chapter selection:",
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
