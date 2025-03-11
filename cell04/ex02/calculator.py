num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 !=0 :
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"
print(f"{num1} + {num2} = {addition}")
print(f"{num1} + {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")