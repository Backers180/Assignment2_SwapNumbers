print("This program will exchange the values of two numbers") 
print("without using a temporary variable")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
  x = x+y
  y = x-y
  x = x-y
  print("Your first number is:", x)
  print("Your second number is:", y)
else:
  y = y+x
  x = y-x
  y = y-x
  print("Your first number is:", x)
  print("Your second number is:", y)