import json

with open("questions12.json", "r") as questions:
    content = questions.read()

data = json.loads(content)

for question in data:
    print(question["questions"])
    for index, alternatives in enumerate(question["options"]):
        print(index + 1, "-", alternatives)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += score
        result = "Correct !"
    else:
        result = "Wrong !"

    message = f'Q{index + 1} is {result} -> Your answer: {question["user_choice"]}, ' \
              f'Correct answer: {question["correct_answer"]}'
    print(message)

# print(data)
print(score, "/", len(data))
