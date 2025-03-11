A = int(input("enter a number less than 25\n"))

if A < 25:
    for i in range(A,26):
        print(f"inside the loop , myvariable is {i}")
else :
    print("error")