import json
import sys
from pathlib import Path


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
    "1.) ALL",
    "2.) PROGRAMMING LANGUAGES",
    "3.) PROGRAMMING FIELDS",
    "4.) WRITING",
    "5.) COMMUNICATION",
    "6.) TECHNICAL SKILLS",
    "7.) PROGRAMMING STUDIOS",
    "x.) CHAPTER SELECT",
]


def display_all_skills(skills):
    print("--- ALL SKILLS ---")
    for learnt_skills in sorted(
        skills.get("learnt_skills", []),
        key=lambda item: rank_order.get(item.get("mastery"), 999),
    ):
        print(
            f"Skill: {learnt_skills['title']} | Category: {learnt_skills['category']} | Mastery: {learnt_skills['mastery']}"
        )
        print("-" * 80)


def display_skills_by_category(skills, target_category):
    print(f"--- {target_category} ---")
    filtered = [
        item
        for item in skills.get("learnt_skills", [])
        if item.get("category") == target_category
    ]
    for item in sorted(
        filtered, key=lambda item: rank_order.get(item.get("mastery"), 999)
    ):
        print(f"Skill: {item['title']} | Mastery: {item['mastery']}")
        print("-" * 80)


def show_skills_menu():
    skills = load_skills()

    while True:
        width = 25

        for item in skill_items:
            print(f"|| {item:<{width}} ||")

        user_choice = (
            input(
                "Choose the number of the skill you wish to view, or X to go back to chapter select: "
            )
            .strip()
            .lower()
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
