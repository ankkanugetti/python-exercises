correct = 0

questions = ["When did the WW1 start?", "When did the WW2 start?", "When did the Soviet Union collapse?"]
correct_answers = ["1914", "1939", "1991"]
user_answers = [False, False, False]

for x in range(len(questions)):
  ans = input(questions[x])
  if(ans == correct_answers[x]):
    user_answers[x] = True

print(user_answers)

print(f"Correct: {correct}")