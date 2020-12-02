number = int(input("Enter the number: "))

print ("Multiplication table of", number)

for y in range(1, number + 1):
  for x in range(1, number + 1):
    print(f"{x * y} ", end = "")
  print (f"")
