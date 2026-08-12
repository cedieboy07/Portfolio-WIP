import json


def load_skills(file_path="db_folder/skills.json"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Databse not found.")
        return {"learnt_skills": []}


def display_all_skills(skills):
    print("--- ALL SKILLS ---")
    for learnt_skills in skills["learnt_skills"]:
        print(f"Skill: {learnt_skills['title']} | Category: {learnt_skills['category']} | Mastery: {learnt_skills['mastery']}")


# def display_languages(skills, target_category):
#     print("--- PROGRAMMING LANGUAGES ---")
#     for item in skills["learnt_skills"]:
#         if item.get("category") == target_category:
#             print(f"Skill: {item['title']} | Mastery: {item['mastery']}")


database = load_skills()

display_all_skills(database)

# display_languages(database, "Programming Language")
    