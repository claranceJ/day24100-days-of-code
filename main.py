import random
print("Infinity Dice")
sides=int(input("How many sides"))
def dice(sides):
  game="yes"
  while game=="yes":
    generate=random.randint(1,sides)
    print(f"You rolled {generate}")
    print()
    play=input("Roll again?: ")
    if play=="no":
      game="no"
    else:
      game="yes"
      sides=int(input("How many sides"))
      continue
    
dice(sides)  


  
  
