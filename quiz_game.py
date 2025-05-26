import random as r

questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "What language is this program written in?", "answer": "python"},
    {"question": "What is the opposite of hot?", "answer": "cold"},
    {"question": "How many days are there in a week?", "answer": "7"}
]

score = 0
r.shuffle(questions)

for i in range(3):

    print(questions[i]["question"])
    user = input("Your answer: ").strip().lower()
    if user == questions[i]["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {questions[i]['answer']}")

print(f"Your final score is: {score} out of 3")