import time
import runpy

print("-" * 80)
print("ABOUT THE AUTHOR")
time.sleep(1.5)
print("-" * 80)

print("Charles Daniel Nevalga, born in 2006, has been a Computer Science student in CIIT College of Innovation and Integrated Technology for 6 terms.\n"
"With a GPU of 3.45 and more than 3 projects in his portfolio, he has proven to be a hard-working student that is striving for a bright future.\n"
"Though a tech major, he is known to be a member of the student organization, Obelisk, as a writer with plans of taking an excecutive role.\n"
"Along with other indulgements such as, Writing, Reading, and Video-Gaming, he holds true to his goal of becoming a Software Developer and his\n"
"dream of becoming a Novelist.")

time.sleep(2.5)
print("-" * 80)
print("<--Cover Page" " | " "Chapter 1-->")

user_chap = input("(< or >): ")

if user_chap == '<':
    runpy.run_path('app.py')
elif user_chap == '>':
	runpy.run_path('chap_1.py')