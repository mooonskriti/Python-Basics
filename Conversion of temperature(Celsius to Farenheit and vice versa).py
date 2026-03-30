#(iv)To convert temperatures to and from Celsius, Fahrenheit.
while True:
    print("1. Celsius")
    print("2. Farenheit")
    ch=int(input("What unit do you want to convert your temperature into?:(1/2)"))
    if ch==1:
        a=float(input("Enter the temperature to be converted into Celsius: "))
        c=(a-32)*(5/9)
        print(a," Farenheit is ", c, " Celsius.")
    elif ch==2:
        b=float(input("Enter the temperature to be converted into Farenheit: "))
        f=(b*(9/5))+32
        print(b," Celsius is ", f, " Farenheit.")
    else:
        print("Invalid Choice.")
    z=(input("Want to convert more temperatures?(y/n): "))
    if z=="n":
        break
