import random
plrnum = int(input("Enter a number between 1 and 20: "))
comnum = random.randint(1,20)

print("Computer's number: " + str(comnum))
print("Player's number: " + str(plrnum))
if plrnum == comnum:
  print("You Won!")
else:
  print("Better luck next time :(")