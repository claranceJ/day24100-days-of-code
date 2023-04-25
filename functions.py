def fizz_buzz(input):
  while True:
    number=int(input("Enter number: "))
    if number%5==0 and number%3==0:
      print("Fizz_buzz")
    elif number%3==0:
      print("buzz")
    elif number%5==0:
      print("fizz")
    else:
      print(f"{number} not divisible by either 5 or 3")
  return number
  
divisible=fizz_buzz(input)
print(divisible)