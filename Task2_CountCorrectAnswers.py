correct = 0
incorrect = 0

print("Here is a little math quiz")
print()
ans = int(input("What is 8 + 3? "))
val = 11
if(ans == val):
  correct + 1
else:
  incorrect + 1
ans = int(input("What is 4 + 6? "))
val = 10
if(ans == val):
  correct + 1
else:
  incorrect + 1
ans = int(input("What is 12 + 8? "))
val = 20
if(ans == val):
  correct + 1
else:
  incorrect + 1
ans = int(input("What is 2 + 7? "))
val = 9
if(ans == "9"):
  correct + 1
else:
  incorrect + 1
ans = int(input("What is 9 + 5? "))
val = 14
if(ans == val):
  correct + 1
else:
  incorrect + 1

print("Correct ones", [correct])