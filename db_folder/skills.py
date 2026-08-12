import json


def load_skills(file_path="db_folder/skills.json"):
    try:
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
        user_skills = (
            input(
                "Do you want to view all skills, specific categories, or return to chapter selection? (all/languages/field/writing/communication/x): "
            )
            .strip()
            .lower()
        )

        if user_skills == "all":
            display_all_skills(skills)
        elif user_skills == "languages":
            display_skills_by_category(skills, "Programming Language")
        elif user_skills == "field":
            display_skills_by_category(skills, "Programming Field")
        elif user_skills == "writing":
            display_skills_by_category(skills, "Writing")
        elif user_skills == "communication":
            display_skills_by_category(skills, "Communication")
        elif user_skills == "x":
            print("Returning to chapter selection...")
            break
        else:
            print(
                "Invalid choice. Please type 'all', 'languages', 'field', 'writing', 'communication', or 'x'."
            )


if __name__ == "__main__":
    show_skills_menu()
