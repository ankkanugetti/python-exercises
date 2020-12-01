Answer1 = input("Do you know where is United States located? Yes or no?")
Answer2 = input ("Do you know when the United States became independent?")
print (f"You said {Answer1} and you guessed {Answer2} to be the year when United States became independent")
Answer2 = int(Answer2)
if (Answer2 is 1776 or 1783):
  print("You were right! Nice job!")
else:
  print("Right answer was 1776 and 1783 because in 1783 they recognized it and in 1776 they declared it")
