number1 = int(input("please enter first number : "))
number2 = int(input("please enter second number : "))

print(str(number1)+" "+"x"+" "+str(number2)+" "+"="+str(number1*number2) )

if number1*number2 < 0 :
    print("the result is negative. ")

elif number1*number2 > 0 :
    print("the result is positive. ")

elif number1*number2 ==0 :
    print("the result is positive and negative. ")