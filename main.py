import random

print("Infinity Dice 🎲")
print()
sides=int(input("How many sides?: "))
rollAgain="yes"

def rollDice(sides):
  roll=random.randint(1, sides)
  print(f"You rolled {roll}")
while rollAgain=="yes":
  rollDice(sides)
  print()
  rollAgain=input("Roll again?: ")
  if rollAgain!="yes":
    print("Goodbye!")
    exit()