questions = ["What is 8 + 3? ", "What is 4 + 6? ", "What is 12 + 8? "]
correct_answers = [11, 10, 20]

correct = 0

for x in range(len(questions)):
  ans = int(input(questions[x]))
  if(ans == correct_answers[x]):
    correct = correct + 1

print(f"Correct: {correct}")
