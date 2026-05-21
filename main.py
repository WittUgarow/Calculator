number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

print("\nWhat would you like to do?\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice = input("Choice:")

if choice=="1":
  print(number1+number2)
elif choice=="2":
  print(number1-number2)
elif choice=="3":
    print(number1*number2)
elif choice=="4":
  print(number1/number2)
else:
  print("Option does not exist")