#To check whether a number is even or odd
n=int(input("Enter a number to check if it's even or odd: "))
if n==0:
    print("The number is zero. Hence, cannot check.")
elif n%2==0:
    print(n, " is an even number.")
else:
    print(n, " is an odd number.")
