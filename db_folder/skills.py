import json
import sys
from pathlib import Path
from assets.terminal_ui import entry, heading, menu


def load_skills(file_path=None):
    try:
        if file_path is None:
            base_path = Path(
                getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[1])
            )
            file_path = base_path / "db_folder" / "skills.json"
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Database not found.")
        return {"learnt_skills": []}


rank_order = {
    "Novice": 0,
    "Beginner": 1,
    "Advanced Beginner": 2,
    "Competent": 3,
    "Proficient": 4,
    "Expert": 5,
}

skill_items = [
    ("1", "All skills"),
    ("2", "Programming languages"),
    ("3", "Programming fields"),
    ("4", "Writing"),
    ("5", "Communication"),
    ("6", "Technical skills"),
    ("7", "Programming studios"),
    ("x", "Return to chapter selection"),
]


def display_all_skills(skills):
    heading("All Skills", "CHAPTER I / CATALOG")
    for learnt_skills in sorted(
        skills.get("learnt_skills", []),
        key=lambda item: rank_order.get(item.get("mastery"), 999),
    ):
        entry(
            learnt_skills["title"],
            [
                ("Category", learnt_skills["category"]),
                ("Rank", learnt_skills["mastery"]),
            ],
        )


def display_skills_by_category(skills, target_category):
    heading(target_category, "CHAPTER I / CATALOG")
    filtered = [
        item
        for item in skills.get("learnt_skills", [])
        if item.get("category") == target_category
    ]
    for item in sorted(
        filtered, key=lambda item: rank_order.get(item.get("mastery"), 999)
    ):
        entry(item["title"], [("Rank", item["mastery"])])


def show_skills_menu():
    skills = load_skills()

    while True:
        user_choice = menu(
            "Skills Index",
            skill_items,
            "Choose a category, or X to return to chapter selection:",
        )

        if user_choice == "1":
            display_all_skills(skills)
        elif user_choice == "2":
            display_skills_by_category(skills, "Programming Language")
        elif user_choice == "3":
            display_skills_by_category(skills, "Programming Field")
        elif user_choice == "4":
            display_skills_by_category(skills, "Writing")
        elif user_choice == "5":
            display_skills_by_category(skills, "Communication")
        elif user_choice == "6":
            display_skills_by_category(skills, "Technical Skill")
        elif user_choice == "7":
            display_skills_by_category(skills, "Programming Studio")
        elif user_choice == "x":
            print("Returning to chapter selection...")
            break
        else:
            print(
                "Invalid choice. Please type '1', '2', '3', '4', '5', '6', '7' or 'x'."
            )


if __name__ == "__main__":
    show_skills_menu()
