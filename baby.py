from random import choice

questions = ["Why is the sky blue?: " , "Why are plants green?: ", "Why do planets orbit the sun?: " ,
             "Why do dogs bark?: ", "Where are all the aliens?: " ]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()
print("Oh..okay")
