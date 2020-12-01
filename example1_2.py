gmail = input("Please enter your gmail")
name = input("Please enter your fullanem")
age = input("Please enter you age")
print(f"Your name is {name}, your gmail is {gmail} and you're {age} years old")
age = int(age)
if (age >= 13):
  print("Welcome to the website, here you can chat with others")
else:
  print("Sorry but you need to be 13 to register here")