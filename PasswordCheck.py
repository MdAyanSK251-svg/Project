password = input("enter the password:")
upper = False
lower = False
digit = False
special = False
for i in password:
  if i.isupper():
    upper = True
  elif i.islower():
    lower = True
  elif i.isdigit():
    digit = True
  else:
    special = True

score = 0
if upper:
  score += 1
if lower:
  score += 1
if digit:
  score += 1
if special:
  score += 1
if len(password)<8:
  print("strong Password")
elif score == 4:
  print("Strong Password")
elif score >= 2:
  print("medium Password")
else:
  print("Weak Password")