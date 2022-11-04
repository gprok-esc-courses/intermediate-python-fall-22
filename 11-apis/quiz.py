import requests
import json

url = 'https://opentdb.com/api.php?amount=10&type=multiple'
response = requests.get(url)

data = json.loads(response.text)

questions = data['results']

score = 0
# Homework: Shuffle answers so that the correct answer is not always on position 1
# but still know the random position of the correct answer and update the score
for row in questions:
    print("Q:", row['question'])
    print("1.", row['correct_answer'])
    counter = 2
    for wrong in row['incorrect_answers']:
        print(str(counter)+".", wrong)
        counter += 1
    answer = input("Your answer? ")

print("SCORE:", score, "/10")
