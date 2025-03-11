user_input = input("enter a number: ")
try:
    num = float(user_input)
    if '_' in user_input:
        print("this is a decimal number")
    else:
        print("this is not decimal number")
except ValueError:
    print("the input is not a valid number.")