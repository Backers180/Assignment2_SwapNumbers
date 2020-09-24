print("This program will exchange the values of two numbers") 
print("without using a temporary variable")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


x = x+y
y = x-y
x = x-y
print("Your first number is:", x)
print("Your second number is:", y)