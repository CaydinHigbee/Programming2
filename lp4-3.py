eggs = int(input("Enter amount of eggs: "))
dozen = eggs / 12
price = 0.0
if dozen >= 0 and dozen < 4:
  price = 0.50
elif dozen >= 4 and dozen < 6:
  price = 0.45
elif dozen >= 6 and dozen < 11:
  price = 0.40
elif dozen >= 11:
  price = 0.35
else:
  print("Enter valid number of eggs")
print("The bill is equal to: $" + str(price * dozen))